# Simple netcat replacement

import socket
import argparse
import logging
import subprocess
import sys
import threading


CONNECTION_BACKLOG = 5
REQUEST_SIZE = 4096
RESPONSE_SIZE = 4096

COMMAND_PROMPT = b"nc > "


# Connects to specified @host and @port,
# sends @buffer and stdin to that host, printing responses
def client_sender(buffer, host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))

        if buffer:
            client.send(buffer.encode("utf-8"))

        while True:
            recv_length = 1
            response = b""

            while recv_length:
                data = client.recv(RESPONSE_SIZE)
                recv_length = len(data)
                response += data

                if recv_length < RESPONSE_SIZE:
                    break

            print(response.decode("utf-8"), end='')

            buffer = input("")
            buffer += "\n"

            client.send(buffer.encode("utf-8"))

    except (ConnectionRefusedError, EOFError, socket.gaierror) as e:
        logging.error(e)
        client.close()


def server_loop(args):
    host = args.target_host
    if not host:
        host = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, args.target_port))
    server.listen(CONNECTION_BACKLOG)

    while True:
        client_socket, client_address = server.accept()
        logging.info(f"Got connection from {client_address}")
        client_thread = threading.Thread(target=client_handler,
                                         args=(client_socket, args))
        client_thread.start()


def run_command(command):
    command = command.strip()
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT,
                                         shell=True)
        return output
    except subprocess.CalledProcessError as e:
        error_message = f"Failed to execute command: {e}.\r\n"
        logging.error(error_message)
        return error_message.encode("utf-8")


def client_handler(client_socket, args):
    if args.upload is not None:
        file_buffer = b""
        while True:
            data = client_socket.recv(REQUEST_SIZE)
            if not data:
                break
            else:
                file_buffer += data
        try:
            with open(args.upload, "wb") as upload_file:
                upload_file.write(file_buffer)
            client_socket.send(f"Successfully saved file to {args.upload}\r\n")
        except IOError as e:
            client_socket.send(f"Failed to save file to {args.upload}\r\n")
            logging.error(e)

    if args.execute is not None:
        output = run_command(args.execute)
        client_socket.send(output)

    if args.command:
        while True:
            try:
                client_socket.send(COMMAND_PROMPT)
                command_buffer = b""

                while b'\n' not in command_buffer:
                    command_continuation = client_socket.recv(REQUEST_SIZE)
                    if not command_continuation:
                        break
                    command_buffer += command_continuation

                response = run_command(command_buffer)
                client_socket.send(response)
            except (BrokenPipeError, ConnectionResetError) as e:
                logging.error(f"Connection reset: {e}")
                break


def main():
    parser = argparse.ArgumentParser(description="netcat replacement")
    parser.add_argument('target_host')
    parser.add_argument('target_port', type=int)
    parser.add_argument('-l', '--listen', action='store_true',
                        help="listen on [target_host]:[target_port] for incoming connections")
    parser.add_argument('-e', '--execute',
                        help="execute the given file upon receiving a connection")
    parser.add_argument('-c', '--command', action='store_true',
                        help="initialize a command shell")
    parser.add_argument('-u', '--upload',
                        help="upon receiving connection upload a file and write to [UPLOAD]")

    args = parser.parse_args()

    if not args.listen and args.target_port > 0:
        buffer = sys.stdin.read()

        client_sender(buffer, args.target_host, args.target_port)

    if args.listen:
        server_loop(args)


if __name__ == '__main__':
    main()

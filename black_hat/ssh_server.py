# SSH server sending commands


import argparse
import logging
import paramiko
import socket
import threading


BUFFER_SIZE = 1024
CONNECTION_BACKLOG = 100
CONNECT_TIMEOUT = 20

PROMPT = "> "

HOST_KEY = paramiko.RSAKey(filename='/usr/share/doc/packages/python3-paramiko/demos/test_rsa.key')


class Server(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if username == '<username>' and password == '<password>':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED


def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("local_host")
    parser.add_argument("local_port", type=int)
    parser.add_argument("-v", "--verbose", action='store_true')

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((args.local_host, args.local_port))

    server_socket.listen(CONNECTION_BACKLOG)
    logging.info("Listening for connection")

    client_socket, client_address = server_socket.accept()
    logging.info(f"Got connection from {client_address}")

    session = paramiko.Transport(client_socket)
    session.add_server_key(HOST_KEY)
    server = Server()
    try:
        session.start_server(server=server)
    except paramiko.SSHException as e:
        logging.error(f"SSH negotiation failed: {e}")

    channel = session.accept(CONNECT_TIMEOUT)
    logging.info("Authenticated!")

    print(channel.recv(BUFFER_SIZE).decode("utf-8"))
    channel.send('Welcome to bh_ssh')

    while True:
        try:
            command = input(PROMPT).strip('\n')
            if not command:
                continue
            if command != 'exit':
                channel.send(command)
                output = channel.recv(BUFFER_SIZE)
                print(output.decode("utf-8"), end='')
            else:
                channel.send('exit')
                logging.info("Exiting")
                session.close()
                return
        except (KeyboardInterrupt, OSError, EOFError) as e:
            logging.error(f"{e}; Exiting")
            session.close()
            break

if __name__ == '__main__':
    main()

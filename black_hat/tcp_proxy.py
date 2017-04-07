# Simple TCP proxy

# TODO: looks like it malfunctions now (repeated timeouts). Why does it happen?

import argparse
import logging
import socket
import threading


CONNECTION_BACKLOG = 5
CONNECTION_TIMEOUT_SEC = 2

BUFFER_SIZE = 4096


def hexdump(buffer, length=16):
    digits = 2
    result = []
    for i in range(0, len(buffer), length):
        s = buffer[i:i+length]
        hexa = ' '.join(f"{x:{digits}X}" for x in s)
        text = ''.join((chr(x) if 0x20 <= x < 0x7f else '.' for x in s))
        result.append(f"{i:04X}    {hexa:{length * (digits + 1)}}   {text}")

    logging.info('\n'.join(result))


def receive_from(connection):
    buffer = b""
    connection.settimeout(CONNECTION_TIMEOUT_SEC)

    try:
        while True:
            data = connection.recv(BUFFER_SIZE)
            if not data:
                break
            buffer += data
    except (socket.timeout,) as e:
        logging.warning(f"Error: {e}")

    return buffer


def response_handler(buffer):
    return buffer


def request_handler(buffer):
    return buffer


def proxy_handler(client_socket, args):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((args.remote_host, args.remote_port))

    if args.receive_first:
        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

        remote_buffer = response_handler(remote_buffer)

        if remote_buffer:
            logging.info(f"<== Sending {len(remote_buffer)} bytes to localhost")
            client_socket.send(remote_buffer)

    while True:
        local_buffer = receive_from(client_socket)

        if local_buffer:
            logging.info(f"==> Received {len(local_buffer)} bytes from localhost.")
            hexdump(local_buffer)

            local_buffer = request_handler(local_buffer)

            remote_socket.send(local_buffer)
            logging.info("==> Sent to remote.")

        remote_buffer = receive_from(remote_socket)

        if remote_buffer:
            logging.info(f"<== Received {len(remote_buffer)} bytes from remote.")
            hexdump(remote_buffer)

            remote_buffer = response_handler(remote_buffer)

            client_socket.send(remote_buffer)
            logging.info("<== Sent to localhost.")

        if not local_buffer or not remote_buffer:
            client_socket.close()
            remote_socket.close()
            logging.info("No more data. Closing connections.")
            break


def server_loop(args):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((args.local_host, args.local_port))

    logging.info(f"Listening on {args.local_host}:{args.local_port}")

    server.listen(CONNECTION_BACKLOG)

    while True:
        client_socket, client_address = server.accept()
        logging.info(f"==> Received incoming connection from {client_address}")
        proxy_thread = threading.Thread(target=proxy_handler,
                                        args=(client_socket, args))
        proxy_thread.start()


def main():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description="TCP proxy")
    parser.add_argument("local_host")
    parser.add_argument("local_port", type=int)
    parser.add_argument("remote_host")
    parser.add_argument("remote_port", type=int)
    parser.add_argument("--receive-first", action='store_true')

    args = parser.parse_args()
    server_loop(args)


if __name__ == '__main__':
    main()

# Multi-threaded TCP server

import logging
import socket
import threading

BIND_IP = "0.0.0.0"
BIND_PORT = 9999
RESPONSE_SIZE = 1024
CONNECTIONS_BACKLOG = 5


# Read and log data send by client and send back response
def handle_client(client_socket, data_to_send):
    request = client_socket.recv(RESPONSE_SIZE)

    logging.info(f"Received: {request.decode('utf-8')}")

    client_socket.send(data_to_send)
    client_socket.close()


def main():
    logging.basicConfig(level=logging.INFO)

    data_to_send = b"ACK!"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(CONNECTIONS_BACKLOG)

    logging.info(f"Listening on {BIND_IP}:{BIND_PORT}")

    while True:
        client, addr = server.accept()

        logging.info(f"Accepted connection from: {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client, data_to_send))
        client_handler.start()


if __name__ == '__main__':
    main()

# Simple TCP client example

import socket

TARGET_HOST = "www.google.com"
TARGET_PORT = 80

RESPONSE_SIZE = 4096


def connect(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    return client


def print_response(s_bytes):
    response_str = s_bytes.decode("utf-8")
    print(response_str)


def main():
    data = b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"

    client = connect(TARGET_HOST, TARGET_PORT)
    client.send(data)
    response = client.recv(RESPONSE_SIZE)

    print_response(response)


if __name__ == '__main__':
    main()

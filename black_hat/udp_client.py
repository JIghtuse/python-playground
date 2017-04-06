# Simple UDP client example

import socket

TARGET_HOST = "127.0.0.1"
TARGET_PORT = 80

RESPONSE_SIZE = 4096


def main():
    data = b"AAABBBCCC"

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(data, (TARGET_HOST, TARGET_PORT))

    data, addr = client.recvfrom(RESPONSE_SIZE)

    print(data.decode("utf-8"))


if __name__ == '__main__':
    main()

# Example of packet sniffing: reading a single packet

import socket
import os


HOST = "127.0.0.1"
PACKET_BUFFER_SIZE = 65565


def main():
    # creating raw socket
    if os.name == "nt":
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP

    sniffer_socket = socket.socket(socket.AF_INET,
                                   socket.SOCK_RAW,
                                   socket_protocol)

    sniffer_socket.bind((HOST, 0))

    # we want the IP headers included in the capture
    sniffer_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # enabling promiscuous mode on Windows
    if os.name == "nt":
        sniffer_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    packet_data = sniffer_socket.recvfrom(PACKET_BUFFER_SIZE)
    print(packet_data)

    if os.name == "nt":
        sniffer_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


if __name__ == '__main__':
    main()

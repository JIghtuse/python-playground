# Example of packet sniffing: decoding IP headers

import os
import socket
import struct
from ctypes import Structure, c_uint8, c_uint16, c_uint32


HOST = "127.0.0.1"
PACKET_BUFFER_SIZE = 65565

PROTOCOL_MAP = {
    1: "ICMP",
    6: "TCP",
    17: "UDP"
}


# IP header

class IPHeader(Structure):
    _fields_ = [
        ("ihl", c_uint8, 4),
        ("version", c_uint8, 4),
        ("tos", c_uint8),
        ("len", c_uint16),
        ("id", c_uint16),
        ("offset", c_uint16),
        ("ttl", c_uint8),
        ("protocol_num", c_uint8),
        ("sum", c_uint16),
        ("src", c_uint32),
        ("dst", c_uint32)
    ]

    def __new__(cls, socket_buffer=None):
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))

        self.protocol = PROTOCOL_MAP.get(self.protocol_num,
                                         str(self.protocol_num))


def main():
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

    try:
        while True:
            # read in a packet
            packet_data = sniffer_socket.recvfrom(PACKET_BUFFER_SIZE)[0]

            ip_header = IPHeader(packet_data[0:20])

            print(f"Protocol: {ip_header.protocol}"
                  f" {ip_header.src_address} -> {ip_header.dst_address}")

    except KeyboardInterrupt:
        if os.name == "nt":
            sniffer_socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)


if __name__ == '__main__':
    main()

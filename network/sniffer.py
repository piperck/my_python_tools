# coding:utf-8
import os
import socket
import struct
from ctypes import *

# 监听的主机IP
host = "192.168.1.100"


# IP头定义
class IP(Structure):
    _fields_ = [
        ("ihl",             c_ubyte, 4),
        ("version",         c_ubyte, 4),
        ("tos",             c_ubyte),
        ("len",             c_ushort),
        ("id",              c_ushort),
        ("offset",          c_ushort),
        ("ttl",             c_ubyte),
        ("protocol_num",    c_ubyte),
        ("sum",             c_ushort),
        ("src",             c_uint),
        ("dst",             c_uint),
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

        # readable ip address
        print self.src, type(self.src)
        print self.dst, type(self.dst)
        print struct.pack("<I", self.src), type(struct.pack("<I", self.src))
        self.src_address = socket.inet_ntoa(struct.pack("<I", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<I", self.dst))

        # type of protocol
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)

if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)

sniffer.bind((host, 0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

try:
    while True:
        raw_buffer = sniffer.recvfrom(65535)[0]

        ip_header = IP(raw_buffer[:20])

        print "Protocol: %s %s -> %s " % (ip_header.protocol, ip_header.src_address, ip_header.dst_address)

except KeyboardInterrupt:
    pass





# coding:utf-8
import socket
import struct
import threading
import time
from netaddr import IPNetwork, IPAddress
from ctypes import *

# 监听的主机IP
host = "192.168.1.100"

# 扫描目标子网
subnet = "192.168.1.0/24"

magic_message = "PYTHONRULES!"

# 批量发送UDP数据包
def udp_sender(subnet, magic_message):
    time.sleep(5)
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for ip in IPNetwork(subnet):
        try:
            sender.sendto(magic_message, ("%s" % ip, 65212))
        except:
            pass


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
        super(Structure, self).__init__()
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}

        # readable ip address
        self.src_address = socket.inet_ntoa(struct.pack("<I", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<I", self.dst))

        # type of protocol
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)


class ICMP(Structure):
    _fields_ = [
        ("type",            c_ubyte),
        ("code",            c_ubyte),
        ("checksum",        c_ushort),
        ("unused",          c_ushort),
        ("next_hop_mtu",    c_ushort),
    ]

    def __new__(self, socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        super(Structure, self).__init__()
        pass


t = threading.Thread(target=udp_sender, args=(subnet, magic_message))
t.start()

# under the linux, only can use ICMP
socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
sniffer.bind((host, 0))
sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

try:
    while True:
        raw_buffer = sniffer.recvfrom(65535)[0]

        ip_header = IP(raw_buffer[:20])

        print "Protocol: %s %s -> %s " % (ip_header.protocol, ip_header.src_address, ip_header.dst_address)

        if ip_header.protocol == "ICMP":
            offset = ip_header.ihl * 4
            buffer = raw_buffer[offset:offset + sizeof(ICMP)]

            icmp_header = ICMP(buffer)

            if icmp_header.code == 3 and icmp_header.type == 3:
                if IPAddress(ip_header.src_address) in IPNetwork(subnet):

                    # confirm ICMP data included in our magic_message
                    if raw_buffer[len(raw_buffer)-len(magic_message):] == magic_message:
                        print "Host down: %s" % ip_header.src_address

except KeyboardInterrupt:
    pass





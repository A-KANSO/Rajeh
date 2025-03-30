import sys
from scapy.all import *

def transmit(message, host):
    for m in message:
        packet = IP(dst=host)/ICMP(code=ord(m))
        send(packet)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python NonApplicationClient.py <host> <message>")
    else:
        host = sys.argv[1]
        message = sys.argv[2]
        transmit(message, host)

import argparse
from scapy.all import *
from scapy.layers.inet import IP, ICMP

def detect_os(target):
    os = ''
    pack = IP(dst=target)/ICMP()
    resp = sr1(pack, timeout=3)
    if resp:
        if IP in resp:
            ttl = resp.getlayer(IP).ttl
            if ttl <= 64: 
                os = 'Linux'
            elif ttl > 64:
                os = 'Windows'
            else:
                os = 'Unknown'
            print(f'\nTTL = {ttl}\n*{os}* Operating System is Detected\n')
    else:
        print("No response received")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect the operating system of a target host based on TTL")
    parser.add_argument("target", help="Specify the target IP address to scan")

    args = parser.parse_args()
    target = args.target

    detect_os(target)

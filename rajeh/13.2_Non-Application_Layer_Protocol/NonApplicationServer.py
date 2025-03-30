from scapy.all import *

def handle_packet(packet):
    if ICMP in packet and packet[ICMP].type == 8:  # Echo request (ping)
        message = chr(packet[ICMP].code)
        print(f"Received message: {message}")

if __name__ == "__main__":
    print("Server is running...")
    sniff(filter="icmp", prn=handle_packet)

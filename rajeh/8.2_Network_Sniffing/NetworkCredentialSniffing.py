import sys
from scapy.all import *
from base64 import b64decode
import re

def ExtractFTP(packet, ftp_port):
    if packet[TCP].dport == ftp_port:
        payload = packet[Raw].load.decode("utf-8").rstrip()
        if payload[:4] == 'USER':
            print("%s FTP Username: %s" % (packet[IP].dst, payload[5:]))
        elif payload[:4] == 'PASS':
            print("%s FTP Password: %s" % (packet[IP].dst, payload[5:]))

emailregex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
unmatched = []
def ExtractSMTP(packet, smtp_port):
    if packet[TCP].dport == smtp_port:
        payload = packet[Raw].load
        try:
            decoded = b64decode(payload).decode("utf-8")
            connData = [packet[IP].src, packet[TCP].sport]
            if re.search(emailregex, decoded):
                print("%s SMTP Username: %s" % (packet[IP].dst, decoded))
                unmatched.append([packet[IP].src, packet[TCP].sport])
            elif connData in unmatched:
                print("%s SMTP Password: %s" % (packet[IP].dst, decoded))
                unmatched.remove(connData)
        except:
            return

awaitingLogin = []
awaitingPassword = []
def ExtractTelnet(packet, telnet_port):
    if packet[TCP].sport == telnet_port or packet[TCP].dport == telnet_port:
        try:
            payload = packet[Raw].load.decode("utf-8").rstrip()
        except:
            return
        connData = [packet[IP].src, packet[TCP].sport] # Assume server is source
        if payload[:5] == "login":
            awaitingLogin.append(connData)
            return
        elif payload[:8] == "Password":
            awaitingPassword.append(connData)
            return
        connData = [packet[IP].dst, packet[TCP].dport] # Assume client is source
        if connData in awaitingLogin:
            print("%s Telnet Username: %s" % (packet[IP].dst, payload))
            awaitingLogin.remove(connData)
        elif connData in awaitingPassword:
            print("%s Telnet Password: %s" % (packet[IP].dst, payload))
            awaitingPassword.remove(connData)

def main():
    if len(sys.argv) != 5:
        print("Usage: python NetworkCredentialSniffing.py <pcap_file_path> <ftp_port> <smtp_port> <telnet_port>")
        sys.exit(1)

    pcap_file_path = sys.argv[1]
    ftp_port = int(sys.argv[2])
    smtp_port = int(sys.argv[3])
    telnet_port = int(sys.argv[4])

    packets = rdpcap(pcap_file_path)

    for packet in packets:
        if packet.haslayer(TCP) and packet.haslayer(Raw):
            ExtractFTP(packet, ftp_port)
            ExtractSMTP(packet, smtp_port)
            ExtractTelnet(packet, telnet_port)

if __name__ == "__main__":
    main()

import argparse
from scapy.all import rdpcap, IP

# Dictionary to store flow data
flowData = {}

def analyzeFlow(p):
    # Check if packet has an IP layer
    if not p.haslayer(IP):
        return

    # Get the length of the IP packet
    length = p[IP].len

    # Create a unique key for the flow based on source and destination IP addresses
    if p[IP].src < p[IP].dst:
        key = ','.join([p[IP].src, p[IP].dst])
        data = [length, 0]
    else:
        key = ','.join([p[IP].dst, p[IP].src])
        data = [0, length]

    # Update flow data
    if key in flowData:
        f = flowData[key]
        flowData[key] = [f[0] + data[0], f[1] + data[1]]
    else:
        flowData[key] = data

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Analyze network flows from a pcap file.')
    parser.add_argument('pcap_file', help='Path to the pcap file')
    args = parser.parse_args()

    # Read packets from the pcap file
    packets = rdpcap(args.pcap_file)

    # Analyze each packet
    for p in packets:
        analyzeFlow(p)

    # Print the flow data
    for f in flowData:
        src, dst = f.split(",")
        d = flowData[f]
        print("%d bytes %s->%s\t%d bytes %s->%s" % (d[0], src, dst, d[1], dst, src))

if __name__ == '__main__':
    main()

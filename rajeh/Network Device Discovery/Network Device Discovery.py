import scapy.all as scapy
from termcolor import colored
import argparse

def scan(ip, timeout=10):  
    try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list, _ = scapy.srp(arp_request_broadcast, timeout=timeout, verbose=False)

        client_list = []
        for _, element in answered_list:
            client_dict = {"ip": element.psrc, "mac": element.hwsrc}
            client_list.append(client_dict)
        return client_list
    except Exception as e:
        print(colored(f"An error occurred: {e}", "red"))
        return []

def print_result(result_list):
    if result_list:
        print("Discovered Devices:")
        print("IP Address\t\tMAC Address")
        print("---------------------------------------")
        for result in result_list:
            print(result["ip"], "\t\t", result["mac"])
    else:
        print(colored("No devices found.", "yellow"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ARP Scanner")
    parser.add_argument("target_ip", help="Specify the target IP address or IP range (in CIDR notation) to scan")
    parser.add_argument("--timeout", type=int, default=10, help="Specify the timeout for ARP requests (in seconds)")
    args = parser.parse_args()

    target_ip = args.target_ip
    timeout_value = args.timeout

    print(f"Scanning network {target_ip} with timeout {timeout_value} seconds...")
    scan_result = scan(target_ip, timeout=timeout_value)
    print_result(scan_result)

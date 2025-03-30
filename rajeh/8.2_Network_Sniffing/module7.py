import tkinter as tk
from tkinter import filedialog
from scapy.all import *

def open_pcap_file():
    filename = filedialog.askopenfilename(filetypes=[("PCAP files", "*.pcap")])
    entry_pcap.delete(0, tk.END)
    entry_pcap.insert(tk.END, filename)

def start_sniffing():
    try:
        ftp_port = int(entry_ftp.get())
        smtp_port = int(entry_smtp.get())
        telnet_port = int(entry_telnet.get())
    except ValueError:
        print("Please enter valid integer values for the ports.")
        return

    pcap_file = entry_pcap.get()
    if not pcap_file:
        print("Please select a PCAP file.")
        return

    packets = rdpcap(pcap_file)
    for packet in packets:
        if packet.haslayer(TCP) and packet.haslayer(Raw):
            if packet[TCP].dport == ftp_port:
                extract_ftp(packet)
            elif packet[TCP].dport == smtp_port:
                extract_smtp(packet)
            elif packet[TCP].sport == telnet_port or packet[TCP].dport == telnet_port:
                extract_telnet(packet)

def extract_ftp(packet):
    payload = packet[Raw].load.decode("utf-8").rstrip()
    if payload.startswith('USER'):
        print("FTP Username:", payload[5:])
    elif payload.startswith('PASS'):
        print("FTP Password:", payload[5:])

def extract_smtp(packet):
    payload = packet[Raw].load
    try:
        decoded = payload.decode("utf-8")
        if '@' in decoded:
            print("SMTP Username:", decoded)
        else:
            print("SMTP Password:", decoded)
    except UnicodeDecodeError:
        pass

def extract_telnet(packet):
    try:
        payload = packet[Raw].load.decode("utf-8").rstrip()
        if payload.startswith("login"):
            print("Telnet Username:", payload)
        elif payload.startswith("Password"):
            print("Telnet Password:", payload)
    except UnicodeDecodeError:
        pass

root = tk.Tk()
root.title("Network Security Scanner")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_pcap = tk.Label(frame, text="PCAP File:")
label_pcap.grid(row=0, column=0, padx=5, pady=5)

entry_pcap = tk.Entry(frame, width=30)
entry_pcap.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(frame, text="Browse", command=open_pcap_file)
button_browse.grid(row=0, column=2, padx=5, pady=5)

label_ports = tk.Label(frame, text="Ports:")
label_ports.grid(row=1, column=0, padx=5, pady=5)

label_ftp = tk.Label(frame, text="FTP:")
label_ftp.grid(row=1, column=1, padx=5, pady=5)

entry_ftp = tk.Entry(frame, width=5)
entry_ftp.grid(row=1, column=2, padx=5, pady=5)

label_smtp = tk.Label(frame, text="SMTP:")
label_smtp.grid(row=1, column=3, padx=5, pady=5)

entry_smtp = tk.Entry(frame, width=5)
entry_smtp.grid(row=1, column=4, padx=5, pady=5)

label_telnet = tk.Label(frame, text="Telnet:")
label_telnet.grid(row=1, column=5, padx=5, pady=5)

entry_telnet = tk.Entry(frame, width=5)
entry_telnet.grid(row=1, column=6, padx=5, pady=5)

button_start = tk.Button(frame, text="Start Sniffing", command=start_sniffing)
button_start.grid(row=2, columnspan=7, padx=5, pady=5)

root.mainloop()

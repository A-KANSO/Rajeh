import tkinter as tk
from tkinter import filedialog
from scapy.all import *
from base64 import b64decode
import binascii
import re
import base64

def open_pcap_file():
    filename = filedialog.askopenfilename(filetypes=[("PCAP files", "*.pcap")])
    entry_pcap.delete(0, tk.END)
    entry_pcap.insert(tk.END, filename)

def process_pcap_file():
    pcap_file = entry_pcap.get()
    if not pcap_file:
        print_to_output("Please select a PCAP file.")
        return

    ftp_port = entry_ftp.get() or 21
    smtp_port = entry_smtp.get() or 25
    telnet_port = entry_telnet.get() or 23

    if not ftp_port or not smtp_port or not telnet_port:
        print_to_output("Please enter values for all ports.")
        return

    try:
        ftp_port = int(ftp_port)
        smtp_port = int(smtp_port)
        telnet_port = int(telnet_port)
    except ValueError:
        print_to_output("Ports must be integer values.")
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

def print_to_output(message):
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, message + "\n")
    output_text.config(state=tk.DISABLED)
    output_text.see(tk.END)

def extract_ftp(packet):
    payload = packet[Raw].load.decode("utf-8").rstrip()
    if payload[:4] == 'USER':
        print_to_output("%s FTP Username: %s" % (packet[IP].dst,payload[5:]))
    elif payload[:4] == 'PASS':
        print_to_output("%s FTP Password: %s" % (packet[IP].dst,payload[5:]))

emailregex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
unmatched = []

def log_error(error_message):
    with open("error_log.txt", "a") as file:
        file.write(error_message + "\n")

# Other functions remain the same...




import base64

def extract_smtp(packet):
    payload = packet[Raw].load
    try:
        # Ensure proper padding for Base64 decoding
        padded_payload = payload + b'=' * ((4 - len(payload) % 4) % 4)
        decoded = base64.b64decode(padded_payload).decode("utf-8")
        connData = [packet[IP].src, packet[TCP].sport]
        if re.search(emailregex, decoded):
            print("%s SMTP Username: %s" % (packet[IP].dst, decoded))
            unmatched.append([packet[IP].src, packet[TCP].sport])
        elif connData in unmatched:
            print("%s SMTP Password: %s" % (packet[IP].dst, decoded))
            unmatched.remove(connData)
    except base64.binascii.Error as e:
        print("Error extracting SMTP data (Base64):", str(e))
    except UnicodeDecodeError as e:
        print("Error decoding SMTP data (Unicode):", str(e))




    
awaitingLogin = []
awaitingPassword = []

def extract_telnet(packet):
    try:
        payload = packet[Raw].load.decode("utf-8").rstrip()
    except:
        return
    connData = [packet[IP].src,packet[TCP].sport] # Assume server is source
    if payload[:5] == "login":
        awaitingLogin.append(connData)
        return
    elif payload[:8] == "Password":
        awaitingPassword.append(connData)
        return
    connData = [packet[IP].dst,packet[TCP].dport] # Assume client is source
    if connData in awaitingLogin:
        print_to_output("%s Telnet Username: %s" % (packet[IP].dst,payload))
        awaitingLogin.remove(connData)
    elif connData in awaitingPassword:
        print_to_output("%s Telnet Password: %s" % (packet[IP].dst,payload))
        awaitingPassword.remove(connData)

root = tk.Tk()
root.title("Network Security Scanner")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_pcap = tk.Label(frame, text="PCAP File:")
label_pcap.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry_pcap = tk.Entry(frame, width=50)
entry_pcap.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(frame, text="Browse", command=open_pcap_file)
button_browse.grid(row=0, column=2, padx=5, pady=5)

label_ports = tk.Label(frame, text="Ports (default):")
label_ports.grid(row=1, column=0, padx=5, pady=5)

label_ftp = tk.Label(frame, text="FTP Port (21):")
label_ftp.grid(row=1, column=1, padx=5, pady=5)

entry_ftp = tk.Entry(frame, width=10)
entry_ftp.grid(row=1, column=2, padx=5, pady=5)

label_smtp = tk.Label(frame, text="SMTP Port (25):")
label_smtp.grid(row=1, column=3, padx=5, pady=5)

entry_smtp = tk.Entry(frame, width=10)
entry_smtp.grid(row=1, column=4, padx=5, pady=5)

label_telnet = tk.Label(frame, text="Telnet Port (23):")
label_telnet.grid(row=1, column=5, padx=5, pady=5)

entry_telnet = tk.Entry(frame, width=10)
entry_telnet.grid(row=1, column=6, padx=5, pady=5)

button_process = tk.Button(frame, text="Process PCAP", command=process_pcap_file)
button_process.grid(row=2, columnspan=7, padx=5, pady=5)

output_frame = tk.Frame(root)
output_frame.pack(padx=20, pady=20)

output_label = tk.Label(output_frame, text="Output:")
output_label.pack(padx=5, pady=5, anchor="w")

output_text = tk.Text(output_frame, width=80, height=20)
output_text.pack(padx=5, pady=5)
output_text.config(state=tk.DISABLED)

root.mainloop()

from email import message
import subprocess
from tkinter import *
import tkinter as tk
from tkinter  import messagebox
import threading
from threading import Thread
from tkinter import filedialog, messagebox, Text, WORD
import os
import re
from tkinter import ttk
from tkinter import font
root =Tk()

# Create a custom font with a larger size
title_font = ("Helvetica", 24)
root.title("Rajeh")



#Running Network Sniffing script and display it
def sniffing_script(new_window, pcap_path, ftp_port, smtp_port, telnet_port):
    script_path = r"C:\Users\user\Desktop\FYP\8.2_Network_Sniffing\NetworkCredentialSniffing.py"
    try:
        # Execute the script using subprocess and catch the output
        output = subprocess.check_output(['python', script_path, pcap_path, ftp_port, smtp_port, telnet_port], universal_newlines=True)
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(tk.END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(tk.END, f"Error: {e}")
#Running File & Directory Discovery script and display it        
def discovery_script(directory, file_types, new_window):
    script_path = r"C:\Users\user\Desktop\FYP\9.2_File_and_Directory_Discovery\FileDiscovery.py"
    try:
        # Execute the script using subprocess and catch the output
        output = subprocess.check_output(['python', script_path, directory, file_types], universal_newlines=True, stderr=subprocess.STDOUT)
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(tk.END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(tk.END, f"Error: {e}")
#Running Network Sniffing script and display it
def start_remote_services(new_window,computer_name, file_path):
     script_path = r"C:\Users\user\Desktop\FYP\10.1_Remote_Services\RemoteServices.py"
     try:
        # Execute the script using subprocess and catch the output
        output= subprocess.check_output(['python', script_path, computer_name, file_path], universal_newlines=True)
        
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
     except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
#Running encrypted server script and display it        
def encrypted_channel_server(new_window, host, port, key):
        def run():
            try:
                server_output_text.config(state=tk.NORMAL)
                server_output_text.delete(1.0, tk.END)
                output = subprocess.check_output(['python', r'C:\Users\user\Desktop\FYP\12.1_Encrypted_Channel\EncryptedChannelServer.py', host, port, key], universal_newlines=True)
                server_output_text.insert(tk.END, output)
            except subprocess.CalledProcessError as e:
                server_output_text.insert(tk.END, f"Server Error: {e}")
            finally:
                server_output_text.config(state=tk.DISABLED)

        server_output_text = tk.Text(new_window, height=10, width=70)
        server_output_text.pack(padx=20, pady=20)
        server_output_text.config(state=tk.DISABLED)

        server_thread = threading.Thread(target=run)
        server_thread.start()
#Running encrypted client script and display it        
def encrypted_channel_client(new_window, host, port, key, message):
        def run():
            try:
                if len(key) not in [16, 24, 32]:
                    raise ValueError("Key must be 16, 24, or 32 bytes long.")
                client_output_text.config(state=tk.NORMAL)
                client_output_text.delete(1.0, tk.END)
                output = subprocess.check_output(['python', r'C:\Users\user\Desktop\FYP\12.1_Encrypted_Channel\EncryptedChannelClient.py', host, port, key, message], universal_newlines=True)
                client_output_text.insert(tk.END, output)
            except subprocess.CalledProcessError as e:
                client_output_text.insert(tk.END, f"Client Error: {e}")
            except ValueError as ve:
                client_output_text.insert(tk.END, f"Client Error: {ve}")
            finally:
                client_output_text.config(state=tk.DISABLED)

        client_output_text = tk.Text(new_window, height=10, width=70)
        client_output_text.pack(padx=5, pady=20)
        client_output_text.config(state=tk.DISABLED)

        client_thread = threading.Thread(target=run)
        client_thread.start()
#Running protocol tunneling  script and display it     
def run_server(script_path,server_output_text, client_finished_event):
    try:
        # Log the start of the server process
        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, "Starting server process...\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)
        
        # Execute the server script using subprocess and catch the output
        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        
        # Log the start of the server script execution
        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, "Server script execution started.\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)
        
        while True:
            output_line = process.stdout.readline()
            if not output_line and process.poll() is not None:
                break
            # Update the GUI with the server output
            server_output_text.config(state=tk.NORMAL)
            server_output_text.insert(tk.END, output_line)
            server_output_text.see(tk.END)
            server_output_text.config(state=tk.DISABLED)
        
        process.wait()  # Wait for the server process to finish
        
        # Log the end of the server script execution
        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, "Server script execution finished.\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)
        
        # Signal that the client has finished
        client_finished_event.set()
        
        # Log that the server process has finished
        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, "Server process finished.\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)
    except Exception as e:
        # Handle any errors that occur during script execution
        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, f"Error: {e}\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)
def protocol_tunneling_server(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\12.2_Protocol_Tunneling\ProtocolTunnelingServer.py"
    server_output_text = Text(new_window, wrap=WORD, width=40, height=10)
    server_output_text.pack()
    server_output_text.config(state=tk.DISABLED)
    
    # Create an event to signal when the client has finished
    client_finished_event = threading.Event()
    
    # Run the server function in a separate thread
    server_thread = threading.Thread(target=run_server, args=(script_path, server_output_text, client_finished_event))
    server_thread.start()
def update_output(output):
    client_output_text.config(state=tk.NORMAL)
    client_output_text.delete(1.0, tk.END)
    client_output_text.insert(tk.END, output)
    client_output_text.config(state=tk.DISABLED)
def protocol_tunneling_client(new_window,url,data):
    
    def run_client(script_path,url,data):
        try:
            # Execute the script using subprocess and catch the output
            output = subprocess.check_output(['python', script_path,url,data], universal_newlines=True)
        
            # Display the output in the Text widget
            new_window.after(0, lambda: update_output(output))
        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during script execution
            new_window.after(0, lambda: update_output(f"Error: {e}"))
    
    script_path = r"C:\Users\user\Desktop\FYP\12.2_Protocol_Tunneling\ProtocolTunnelingClient.py"
    global client_output_text
    client_output_text = Text(new_window, wrap=WORD, width=40, height=10)
    client_output_text.pack()
    client_output_text.config(state=tk.DISABLED)
    
    # Run the client function in a separate thread
    client_thread = threading.Thread(target=run_client, args=(script_path,url,data))
    client_thread.start()  
#Running DNS Exfiltrate script and display it
def run_server(script_path, server_output_text, client_finished_event):
    try:
        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, "Starting server process...\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)

        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, "Server script execution started.\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)

        while True:
            output_line = process.stdout.readline()
            if not output_line and process.poll() is not None:
                break
            server_output_text.config(state=tk.NORMAL)
            server_output_text.insert(tk.END, output_line)
            server_output_text.see(tk.END)
            server_output_text.config(state=tk.DISABLED)

        process.wait()

        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, "Server script execution finished.\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)

        client_finished_event.set()

        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, "Server process finished.\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)
    except Exception as e:
        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, f"Error: {e}\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)
def DNS_exfiltration_server(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\13.1_Alternative_Protocol\DNSExfiltrationServer.py"
    server_output_text = Text(new_window, wrap=WORD, width=40, height=10)
    server_output_text.pack()
    server_output_text.config(state=tk.DISABLED)

    client_finished_event = threading.Event()
    threading.Thread(target=run_server, args=(script_path, server_output_text, client_finished_event)).start()
def update_output(output):
    client_output_text.config(state=tk.NORMAL)
    client_output_text.delete(1.0, tk.END)
    client_output_text.insert(tk.END, output)
    client_output_text.config(state=tk.DISABLED)
def run_client(script_path, ip, site, message, port, new_window):
    try:
        output = subprocess.check_output(['python', script_path, ip, site, message, str(port)], universal_newlines=True)
        new_window.after(0, lambda: update_output(output))
    except subprocess.CalledProcessError as e:
        new_window.after(0, lambda: update_output(f"Error: {e}"))
def DNS_exfiltration_client(new_window, ip, site, message, port):
    script_path = r"C:\Users\user\Desktop\FYP\13.1_Alternative_Protocol\DNSExfiltration.py"
    global client_output_text
    client_output_text = Text(new_window, wrap=WORD, width=40, height=10)
    client_output_text.pack()
    client_output_text.config(state=tk.DISABLED)

    client_thread = threading.Thread(target=run_client, args=(script_path, ip, site, message, port, new_window))
    client_thread.start()
#Running non app server/client script and display it        
def run_server(script_path, server_output_text, client_finished_event):
    try:
        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, "Starting server process...\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)
        
        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        
        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, "Server script execution started.\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)
        
        def read_server_output():
            while True:
                output_line = process.stdout.readline()
                if output_line:
                    server_output_text.config(state=tk.NORMAL)
                    server_output_text.insert(tk.END, output_line)
                    server_output_text.see(tk.END)
                    server_output_text.config(state=tk.DISABLED)
                if process.poll() is not None:
                    break
        
        output_thread = threading.Thread(target=read_server_output, daemon=True)
        output_thread.start()
        
        # Wait for the client to finish
        client_finished_event.wait()

        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, "Client script execution finished. Reading remaining server output...\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)

        # Ensure all remaining output is read
        output_thread.join()
        process.wait()

        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, "Server script execution finished.\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)
    except Exception as e:
        server_output_text.config(state=tk.NORMAL)
        server_output_text.insert(tk.END, f"Error: {e}\n")
        server_output_text.see(tk.END)
        server_output_text.config(state=tk.DISABLED)
def non_app_layer_protocol_server(new_window, client_finished_event):
    script_path = r"C:\Users\user\Desktop\FYP\13.2_Non-Application_Layer_Protocol\NonApplicationServer.py"
    server_output_text = Text(new_window, wrap=WORD, width=40, height=10)
    server_output_text.pack()
    server_output_text.config(state=tk.DISABLED)
    
    server_thread = threading.Thread(target=run_server, args=(script_path, server_output_text, client_finished_event))
    server_thread.start()
def update_output(output):
    client_output_text.config(state=tk.NORMAL)
    client_output_text.delete(1.0, tk.END)
    client_output_text.insert(tk.END, output)
    client_output_text.config(state=tk.DISABLED)
def non_app_layer_protocol_client(new_window, ip_entry, data_entry, client_finished_event):
    def run_client(script_path, ip_entry, data_entry):
        try:
            output = subprocess.check_output(['python', script_path, ip_entry, data_entry], universal_newlines=True)
            new_window.after(0, lambda: update_output(output))
        except subprocess.CalledProcessError as e:
            new_window.after(0, lambda: update_output(f"Error: {e}"))
        finally:
            client_finished_event.set()

    script_path = r"C:\Users\user\Desktop\FYP\13.2_Non-Application_Layer_Protocol\NonApplicationClient.py"
    global client_output_text
    client_output_text = Text(new_window, wrap=WORD, width=40, height=10)
    client_output_text.pack()
    client_output_text.config(state=tk.DISABLED)
    
    client_thread = threading.Thread(target=run_client, args=(script_path, ip_entry, data_entry))
    client_thread.start()
#Running data encryption script and display it     
def encrypt_data(new_window, key, directory, ext):
    script_path = r"C:\Users\user\Desktop\FYP\14.1_Data_Encryption\DataEncryption.py"
    try:
        # Execute the script using subprocess and pass command-line arguments
        output = subprocess.check_output(['python', script_path, key, directory, ext], universal_newlines=True)
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
        output_text.insert(END, f"Error: {e}")
#Running data decryption script and display it  
def decrypt_data(new_window, key, directory):
    script_path = r"C:\Users\user\Desktop\FYP\14.1_Data_Encryption\DataDecryption.py"
    try:
        # Execute the script using subprocess and pass command-line arguments
        output = subprocess.check_output(['python', script_path, key, directory], universal_newlines=True)
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
        output_text.insert(END, f"Error: {e}")
#Running Decoy content script and display it        
def decoy_content(new_window,file):
    script_path=r"C:\Users\user\Desktop\FYP\15.2_Decoy_Content\DecoyContent.py"
    try:
        # Execute the script using subprocess and catch the output
        output=subprocess.check_output(['python',script_path,file],universal_newlines=True)
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, f"Error: {e}")
#Running Burn in script and display it
def burn_in(new_window, file, clickthrough, sleeptime):
    # Ensure clickthrough and sleeptime are valid float and integer respectively
    try:
        clickthrough = clickthrough if clickthrough else 0.9
        sleeptime = sleeptime if sleeptime else 0
    except ValueError as e:
        # Handle the case where clickthrough or sleeptime couldn't be converted to float or integer
        error_message = f"Error: {e}"
        if hasattr(new_window, 'output_text'):
            new_window.output_text.insert(tk.END, error_message)
        else:
            print(error_message)
        return

    def execute_script():
        script_path = r"C:\Users\user\Desktop\FYP\16.3_Burn_In\BurnIn.py"
        try:
            # Execute the script using subprocess and catch the output
            output = subprocess.check_output(['python', script_path, file, str(clickthrough), str(sleeptime)], universal_newlines=True)
            
            # Update the Text widget with the output
            if hasattr(new_window, 'output_text'):
                new_window.output_text.insert(tk.END, output)
            else:
                print(output)
        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during script execution
            error_message = f"Error: {e}"
            if hasattr(new_window, 'output_text'):
                new_window.output_text.insert(tk.END, error_message)
            else:
                print(error_message)

    # Create a Text widget for displaying the output if it doesn't exist
    if not hasattr(new_window, 'output_text'):
        new_window.output_text = tk.Text(new_window, wrap=tk.WORD, width=70, height=30)
        new_window.output_text.pack()

    # Create a new thread to execute the script
    script_thread = threading.Thread(target=execute_script)
    script_thread.start()
#Running network monitoring script and display it
def network_monitoring(new_window,file):
    script_path = r"C:\Users\user\Desktop\FYP\17.1_Network_Monitoring\NetworkMonitoring.py"
    try:
        # Execute the script using subprocess and catch the output
        output= subprocess.check_output(['python', script_path,file], universal_newlines=True)
        
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
        output_text.insert(END, f"Error: {e}")
#Running behavioral analysis script and display it
def behavioral_analysis(new_window, threshold, baseline_time):
    script_path = r"C:\Users\user\Desktop\FYP\BehavioralAnalytics\BehavioralAnalytics.py"
    try:
        # Execute the script using subprocess and catch the output
        output = subprocess.check_output(['python', script_path, '--threshold', str(threshold), '--baseline_time', str(baseline_time)], universal_newlines=True)
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
        output_text.insert(END, f"An error occurred: {e.output}")
#Running local email account script and display it
def local_email_account(new_window,file):
    script_path = r"C:\Users\user\Desktop\FYP\LocalEmailAccounts\LocalEmailAccounts.py"
    try:
        # Execute the script using subprocess and catch the output
        output= subprocess.check_output(['python', script_path,file], universal_newlines=True)
        
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
#Running modify clipboard script and display it
def modify_clipboard(new_window, sensitive_info_type, replacement_text):
    script_path = r"C:\Users\user\Desktop\FYP\ModifyClipboard\ModifyClipboard.py"
    regex_patterns = {
        'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'phone': r'\b(?:\d{3}[-.]?|\(\d{3}\) )?\d{3}[-.]?\d{4}\b',
        'url': r'\bhttps?://\S+\b',
        'date': r'\b\d{1,2}/\d{1,2}/\d{4}\b',
        'ip': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        'credit_card': r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b',
        'ssn': r'\b\d{3}-\d{2}-\d{4}\b'
    }
    pattern = regex_patterns.get(sensitive_info_type)
    if pattern is None:
        messagebox.showerror("Error", "Invalid type of sensitive information selected.")
        return
    try:
        # Execute the script using subprocess and catch the output
        output = subprocess.check_output(['python', script_path, '--type', sensitive_info_type, '--replacement', replacement_text], universal_newlines=True)
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
#Running userdiscovery script and display it
def user_discovery(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\UserDiscovery\UserDiscovery.py"
    try:
        # Execute the script using subprocess and catch the output
        output= subprocess.check_output(['python', script_path], universal_newlines=True)
        
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
#Running accountaccessremoval script and display it
def access_removal(new_window,computer,user,password):
    script_path = r"C:\Users\user\Desktop\FYP\AccountAccessRemoval\AccountAccessRemoval.py"
    try:
        # Execute the script using subprocess and catch the output
        output= subprocess.check_output(['python', script_path,computer,user,password], universal_newlines=True)
        
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()   
#Running sysactivitymonitoring script and display it
def sys_activity_monitoring(new_window, server, logtype, event_id):
    script_path = r"C:\Users\user\Desktop\FYP\SystemActivityMonitoring\SystemActivityMonitoring.py"
    event_id_descriptions = {
    4672: "Special privileges assigned to new logon.",
    4624: "An account was successfully logged on.",
    4634: "An account was logged off.",
    4648: "A logon was attempted using explicit credentials.",
    4768: "A Kerberos authentication ticket (TGT) was requested.",
    4771: "Kerberos pre-authentication failed.",
    4776: "The computer attempted to validate the credentials for an account.",
    4781: "The name of an account was changed.",
    4798: "A user's local group membership was enumerated."}
    event_id = int(event_id)  # Convert to integer
    try:
        # Execute the script using subprocess and catch the output
        output = subprocess.check_output(['python', script_path, '--server', server, '--logtype', logtype, '--event_id', str(event_id)], universal_newlines=True)

        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
        output_text.insert(END, f"Event ID {event_id}: {event_id_descriptions.get(event_id, 'Unknown Event ID')}\n")
        output_text.insert(END, output)

    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
        output_text.insert(END, f"An error occurred: {e.output}")

    except FileNotFoundError as e:
        # Handle file not found errors
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
        output_text.insert(END, f"Script not found: {script_path}")

    except Exception as e:
        # Handle any other exceptions
        output_text = Text(new_window, wrap=WORD, width=50, height=10)
        output_text.pack()
        output_text.insert(END, f"An unexpected error occurred: {str(e)}")
#Running portscanner script and display it
def port_scanner(new_window, host):
    # Class to manage the output window
    class NewWindow:
        def __init__(self):
            self.output_text = Text(new_window, wrap=WORD, width=70, height=20)
            self.output_text.pack(pady=10)

        # Function to update the output text
        def update_text(self, text):
            self.output_text.insert(END, text)
            self.output_text.see(END)  # Auto-scroll to the end

    # Create an instance of the NewWindow class
    new_window_instance = NewWindow()

    # Function to execute the port scanning script
    def run_port_scanner():
        script_path = r"C:\Users\user\Desktop\FYP\PortScanner\Portscanner.py"
        try:
            # Execute the script using subprocess and catch the output
            output = subprocess.check_output(['python', script_path, host], universal_newlines=True)
            
            # Update the GUI with the output
            new_window_instance.update_text(output)
            
        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during script execution
            new_window_instance.update_text(str(e))

    # Create a new thread for running the port scanner
    scanner_thread = threading.Thread(target=run_port_scanner)
    scanner_thread.start()
#Running os detection script and display it
def os_detection(new_window, target_ip):
    script_path = r"C:\Users\user\Desktop\FYP\os detection\os detection.py"
    try:
        # Execute the script using subprocess and catch the output
        output = subprocess.check_output(['python', script_path, target_ip], universal_newlines=True)
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=20)
        output_text.pack(pady=10)
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=70, height=20)
        output_text.pack(pady=10)
        output_text.insert(END, str(e))
#Running network device discovery script and display it
def network_device_discovery(new_window,ip_range, timeout):
    def execute_script():
        script_path = r"C:\Users\user\Desktop\FYP\Network Device Discovery\Network Device Discovery.py"
        try:
            # Execute the script using subprocess and catch the output
            output = subprocess.check_output(['python', script_path, ip_range,'--timeout', timeout], universal_newlines=True)

            # Display the output in the Text widget
            new_window.output_text = Text(new_window, wrap=WORD, width=50, height=10)
            new_window.output_text.pack()
            new_window.output_text.insert(END, output)

        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during script execution
            new_window.output_text = Text(new_window, wrap=WORD, width=50, height=10)
            new_window.output_text.pack()
            new_window.output_text.insert(END, f"An error occurred: {e}")

    # Create a thread to execute the script
    thread = Thread(target=execute_script)
    thread.start()   














#Open a new window when i click button for network sniffing
def open_new_window1():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("600x400")
    label = tk.Label(new_window, text="Network Sniffing", font=("Helvetica", 16))
    label.pack()
    
    description_text = "This tool is a network credential sniffer implemented in Python using the Scapy library.It aims\n  to analyze network traffic captured in a PCAP file to identify and extract sensitive information\n such as FTP usernames and passwords, SMTP usernames, and telnet usernames and passwords."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_network_sniffing_protections():
       protections_text = """
       Network Sniffing Protections:
    
       1. Use Encrypted Communication Protocols:
          - Implement HTTPS for web communications to encrypt data in transit.
          - Use VPNs to encrypt all internet traffic between your device and the VPN server.

       2. Use Strong Wi-Fi Security:
          - Use WPA3 (or at least WPA2) for your Wi-Fi network with a strong, unique password.

       3. Secure Protocols:
          - Use secure versions of protocols such as SFTP instead of FTP, SMTPS instead of SMTP, and SSH instead of Telnet.

       4. Network Segmentation:
          - Segment your network to limit access and reduce the potential for sniffing sensitive data.

       5. Monitor Network Traffic:
          - Regularly monitor network traffic for any suspicious activity and respond promptly to potential threats.

       6. Keep Systems Updated:
          - Ensure all systems and software are up-to-date with the latest security patches to protect against known vulnerabilities.
       
       7.Intrusion Detection and Prevention Systems (IDPS): 
          - Deploying IDPS solutions helps detect and block suspicious network traffic, including attempts at network sniffing.
       """
       network_sniffing_label.config(text=protections_text)
    def open_file_dialog(entry):
      file_path = filedialog.askopenfilename(filetypes=[("PCAP files", "*.pcap"), ("All files", "*.*")])
      entry.delete(0, tk.END)
      entry.insert(0, file_path)

    # Entry for PCAP file path with a button to open file dialog
    pcap_label = tk.Label(new_window, text="Select PCAP file:")
    pcap_label.pack()
    pcap_entry = tk.Entry(new_window, width=50)
    pcap_entry.pack()
    pcap_button = tk.Button(new_window, text="Browse", command=lambda: open_file_dialog(pcap_entry))
    pcap_button.pack()

    # Entry for FTP port
    ftp_label = tk.Label(new_window, text="Enter FTP port:")
    ftp_label.pack()
    ftp_entry = tk.Entry(new_window, width=10)
    ftp_entry.pack()

    # Entry for SMTP port
    smtp_label = tk.Label(new_window, text="Enter SMTP port:")
    smtp_label.pack()
    smtp_entry = tk.Entry(new_window, width=10)
    smtp_entry.pack()

    # Entry for Telnet port
    telnet_label = tk.Label(new_window, text="Enter Telnet port:")
    telnet_label.pack()
    telnet_entry = tk.Entry(new_window, width=10)
    telnet_entry.pack()

    # Create a button in the new window
    button_in_new_window = tk.Button(new_window, text="Start now", command=lambda: sniffing_script(new_window, pcap_entry.get(), ftp_entry.get(), smtp_entry.get(), telnet_entry.get()))
    button_in_new_window.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    
    network_sniffing_button = tk.Button(new_window, text="Network Sniffing Protections", command=display_network_sniffing_protections)
    network_sniffing_button.pack()

    # Create a label to display the protections against network sniffing
    network_sniffing_label = tk.Label(new_window, text="", justify="left")
    network_sniffing_label.pack()  
#Open a new window when i click button for file and directory discovery 
def open_new_window2():
    def browse_directory():
        directory = filedialog.askdirectory()
        entry_directory.delete(0, END)
        entry_directory.insert(0, directory)

    def start_discovery():
        directory = entry_directory.get()
        file_types = entry_file_types.get()
        discovery_script(directory, file_types, new_window)


    def display_protections():
      protections_text = """
      1. Access Controls:
         - Ensure that directory listings are disabled on web servers and file-sharing services to prevent unauthorized users from browsing directories.
         - Set appropriate permissions on files and directories to restrict access only to authorized users.

      2. Directory Whitelisting:
         - Implement directory whitelisting to restrict access to only known directories. This prevents attackers from accessing sensitive directories.

      3. Input Validation and Sanitization:
         - Validate and sanitize user input to prevent directory traversal attacks, where attackers can manipulate input to access directories outside of the intended scope.

      4. Server Hardening:
         - Harden the server by disabling unnecessary services, keeping software up-to-date, and using firewalls to restrict access to only necessary ports and services.

      5. File Encryption:
         - Encrypt sensitive files to ensure that even if they are discovered, they cannot be accessed without the decryption key.

      6. Regular Security Audits:
         - Conduct regular security audits and vulnerability assessments to identify and remediate any weaknesses in your file and directory security measures.

      7. User Education:
         - Educate users about the importance of file and directory security and the risks associated with exposing sensitive information.

      8. Use of Web Application Firewalls (WAFs):
         - Deploy WAFs to protect against common web-based attacks, including directory traversal and file disclosure vulnerabilities.
      """
      protections_label.config(text=protections_text)

    new_window = Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="File & Directory Discovery", font=("Helvetica", 16))
    label.pack()

    description_text = "This tool is designed to search through specified directories for files containing personally \nidentifiable information (PII) such as email addresses, phone numbers, and social security \nnumbers (SSNs). It supports searching through .docx files and any other text-based files \nspecified by the user. The tool reads the contents of these files, applies regular expressions \nto find PII, and prints out any matches along with the file paths."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    label_directory = Label(new_window, text="Directory Path:")
    label_directory.pack()
    entry_directory = Entry(new_window, width=50)
    entry_directory.pack()
    button_browse = Button(new_window, text="Browse", command=browse_directory)
    button_browse.pack()

    label_file_types = Label(new_window, text="File Types (comma-separated):")
    label_file_types.pack()
    entry_file_types = Entry(new_window, width=50)
    entry_file_types.pack()
    entry_file_types.insert(END, ".txt,.docx,.csv")  # Set default file types here

    button_in_new_window = Button(new_window, text="Start now", command=start_discovery)
    button_in_new_window.pack()   
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    additional_button = tk.Button(new_window, text="Protection Against File and Directory Discovery", command=display_protections)
    additional_button.pack()
    protections_label = tk.Label(new_window, text="", justify="left")
    protections_label.pack()
#Open a new window when i click button for remote services
def open_new_window3():
    def browse_file(entry):
     filename = filedialog.askopenfilename()
     entry.delete(0, tk.END)
     entry.insert(tk.END, filename)
    
    new_window = tk.Toplevel(root)
    new_window.title("Remote Services")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="Remote Services", font=title_font)
    label.pack()
    
    description_text = "This tool is designed to remotely manage and run scripts on another Windows computer. It \nfirst enables special administrative access on the remote computer. Then, it connects to \nthat computer, transfers a specific file, and runs it. While it can be used for legitimate \nadministrative tasks, it also has the potential to be used for harmful activities, such as \nrunning malicious software on the remote machine."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_protections():
       protections_text = """
    Remote Services Protections:

    1. Network Segmentation: 
       - Segment your network to isolate critical systems and limit access to administrative shares and other sensitive resources.

    2. Firewalls and Network ACLs: 
       - Implement firewalls and network access control lists (ACLs) to restrict inbound and outbound traffic to only necessary ports and protocols.

    3. Strong Authentication: 
       - Enforce strong authentication mechanisms, such as complex passwords or multi-factor authentication (MFA), to prevent unauthorized access to administrative shares.

    4. Least Privilege: 
       - Limit user privileges to only what is necessary for their roles and responsibilities, reducing the potential impact of unauthorized access.

    5. Disable Unnecessary Services: 
       - Disable or uninstall unnecessary services and features, such as administrative shares (e.g., C$, ADMIN$) on endpoints, to reduce the attack surface.

    6. Regular Patching and Updates: 
       - Keep all systems and software up-to-date with the latest security patches to mitigate known vulnerabilities that could be exploited by attackers.

    7. Monitoring and Logging:
       - Implement robust monitoring and logging mechanisms to detect suspicious activities, such as unauthorized access attempts or changes to system configurations.
    
    8. Access Controls: 
       - Implementing granular access controls ensures that only authorized users or devices can access specific remote services, reducing the risk of unauthorized access or misuse.

    9. Network Intrusion Detection Systems (NIDS): 
       - Deploying NIDS helps detect and block suspicious network traffic targeting remote services, enhancing the network's overall security posture.

    """
       protections_label.config(text=protections_text)
    
       
    computer_name_label = tk.Label(new_window, text="Computer Name:")
    computer_name_label.pack()
    computer_name_entry = tk.Entry(new_window)
    computer_name_entry.pack()
    
    
    file_path_label = tk.Label(new_window, text="File Path:")
    file_path_label.pack()
    file_path_entry = tk.Entry(new_window)
    file_path_entry.pack()
    
    
    browse_button = tk.Button(new_window, text="Browse", command=lambda: browse_file(file_path_entry))
    browse_button.pack()
    
    start_button = tk.Button(new_window, text="Start Services", 
                             command=lambda: start_remote_services(new_window,computer_name_entry.get(), file_path_entry.get()))
    start_button.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    
    remote_services_button = tk.Button(new_window, text="Remote Services Protections", command=display_protections)
    remote_services_button.pack()

    # Create a label to display the protections 
    protections_label = tk.Label(new_window, text="", justify="left")
    protections_label.pack()
#Open a new window when i click button for encrypted channel
def open_new_window4():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x400")
    label = tk.Label(new_window, text="Encrypted Channel", font=title_font)
    label.pack()

    description_text = "This tool includes a server and client script that enable encrypted communication using \nAES encryption in Python. The server listens for connections, receives encrypted messages, \ndecrypts them, and prints the plaintext. The client connects to the server, encrypts a \nmessage using AES with a random initialization vector (IV), and sends the IV, message \nlength, and encrypted data. This setup ensures secure data transmission, protecting \nmessages from being intercepted and read by unauthorized users."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_protections():
       protections_text = """
    Protections against potential attacks targeting the encrypted communication:

    1. Secure Key Management: 
       - Ensure that encryption keys are securely generated, stored, and exchanged between the communicating parties. 
       -Use strong and randomly generated keys, and employ secure key management practices such as key rotation and key revocation.

    2. Integrity Protection: 
       - Include message integrity checks, such as cryptographic hash functions or Message Authentication Codes (MACs), to detect 
         tampering or modification of encrypted messages during transmission.

    3. Secure Transport Layer: 
       - Use a secure transport layer protocol such as TLS (Transport Layer Security) or SSL (Secure Sockets Layer) to establish secure communication channels. 
         These protocols provide encryption, authentication, and integrity protection for data transmitted over the network.

    4. Firewall and Intrusion Detection/Prevention Systems: 
       - Deploy firewalls and intrusion detection/prevention systems (IDS/IPS) to monitor network traffic and detect potential attacks 
         targeting the communication channel. Configure rules to block or alert on suspicious activities.

    5. Limit Network Exposure: 
       - Minimize the exposure of the communication endpoints to the internet by placing them behind firewalls or using network segmentation.
       - Restrict access to only trusted sources and services.
"""
      
       protections_label.config(text=protections_text)
    

    # Host entry
    host_label = tk.Label(new_window, text="Host:")
    host_label.pack()
    host_entry = tk.Entry(new_window)
    host_entry.pack()

    # Port entry
    port_label = tk.Label(new_window, text="Port:")
    port_label.pack()
    port_entry = tk.Entry(new_window)
    port_entry.pack()

    # Key entry
    key_label = tk.Label(new_window, text="Key (16, 24, or 32 bytes):")
    key_label.pack()
    key_entry = tk.Entry(new_window)
    key_entry.pack()

    # Message entry (only needed for client)
    message_label = tk.Label(new_window, text="Message:")
    message_label.pack()
    message_entry = tk.Entry(new_window)
    message_entry.pack()

    # Create a button in the new window for the encrypted channel server
    button_in_new_window = tk.Button(new_window, text="Encrypted Channel Server", command=lambda: encrypted_channel_server(new_window, host_entry.get(), port_entry.get(), key_entry.get()))
    button_in_new_window.pack()

    # Create a button in the new window for the encrypted channel client
    button_in_new_window = tk.Button(new_window, text="Encrypted Channel Client", command=lambda: encrypted_channel_client(new_window, host_entry.get(), port_entry.get(), key_entry.get(), message_entry.get()))
    button_in_new_window.pack()
    

    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    
    encrypted_channel_button = tk.Button(new_window, text="Attacking Encrypted Channel Protections", command=display_protections)
    encrypted_channel_button.pack()

    # Create a label to display the protections 
    protections_label = tk.Label(new_window, text="", justify="left")
    protections_label.pack()
#open a new window when i click button for Protocol tunneling
def open_new_window5():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="Protocol Tunneling",font=title_font)
    label.pack()
    
    description_text = "This tool includes a command-and-control (C2) server and a client for secure communication. \nThe server listens for HTTP GET requests on port 8440 and expects a Base64-encoded \nmessage in the Cookie header. If the message is C2 data, it responds with a Base64-\nencoded Received message; otherwise, it returns a 404 error. The client sends the \nencoded message to the server and prints the server's decoded response. This setup \ndemonstrates a basic C2 communication system."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    def display_protocol_tunneling_protections():
       protections_text = """
    Protections against Protocol tunneling attack:

      1.Network Segmentation:
        Implement strict network segmentation to limit the ability of malware to communicate with its C2 server. Only allow necessary communication channels.
      
      2.Firewall Rules:
        - Use firewall rules to block outbound traffic to known malicious IP addresses or domains.
        - Restrict access to external services that are not needed for regular operations.

      3.Intrusion Detection/Prevention Systems (IDS/IPS):
        - Deploy IDS/IPS to monitor network traffic for suspicious patterns that match known C2 communication signatures.
        - Use systems like Snort or Suricata with updated rule sets to detect C2 traffic.

      4.Endpoint Detection and Response (EDR):
        - Deploy EDR solutions to detect and respond to malicious activities on endpoints, including attempts to establish C2 communications.
"""
      
       protections_label.config(text=protections_text)
    #Create a button in the new widow
    #for protocol tunneling server
    button_in_new_window = tk.Button(new_window, text="Protocol Tunneling Server",command=lambda:protocol_tunneling_server(new_window))
    button_in_new_window.pack()
    
    url_label = tk.Label(new_window, text="Enter URL:")
    url_label.pack()
    url_entry = tk.Entry(new_window, width=50)
    url_entry.pack()

    
    data_label = tk.Label(new_window, text="Enter data:")
    data_label.pack()
    data_entry = tk.Entry(new_window, width=60)
    data_entry.pack()
    #for protocol tunneling client
    button_in_new_window = tk.Button(new_window, text="Protocol Tunneling Client",command=lambda:protocol_tunneling_client(new_window,url_entry.get(),data_entry.get()))
    button_in_new_window.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    protocol_tunneling_button = tk.Button(new_window, text="Protections Against Protocol Tunneling ", command=display_protocol_tunneling_protections)
    protocol_tunneling_button.pack()

    # Create a label to display the protections 
    protections_label = tk.Label(new_window, text="", justify="left")
    protections_label.pack()
#open a new window when i click button for DNS exfiltration
def open_new_window6():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="DNS exfiltration",font=title_font)
    label.pack()
    
    description_text = "DNS tunneling is an attack where data is covertly exfiltrated from a compromised system by encoding \nit into DNS queries. The attacker uses a malicious DNS server to receive these queries, decode the data, and send control \nsignals back to the compromised system. This method leverages the often unmonitored nature of DNS traffic to \nevade traditional security measures."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    

    def display_dns_exfiltration_protections():
       protections_text = """
    Protections against DNS Extrafiltration:

    1. DNS Filtering and Monitoring:
       Implement DNS filtering solutions to block known malicious domains and enforce DNS request policies.
       Regularly monitor DNS traffic for unusual patterns, such as high volumes of requests to specific domains 
       or subdomains, which can indicate tunneling activity.

    2. Firewalls and Intrusion Detection Systems (IDS):
       Configure firewalls to block unauthorized outbound DNS traffic and implement IDS/IPS that can
       detect and alert on suspicious DNS traffic.

    3. Rate Limiting and Throttling:
       Apply rate limiting to DNS requests to reduce the risk of data exfiltration through high-volume DNS queries.

    4. Anomaly Detection:
       Use machine learning and anomaly detection systems to identify deviations from normal DNS traffic patterns. 
       Implement behavior-based monitoring to detect unusual activity, such as spikes in DNS query volume or unusual subdomain structures.

    5. Least Privilege Principle:
       Restrict DNS access to only those users and systems that need it. Implement strict access controls to minimize exposure
       and reduce the risk of DNS tunneling being used for data exfiltration.

    6. Secure DNS Services:
       Use secure DNS services like DNS over HTTPS (DoH) or DNS over TLS (DoT) to encrypt DNS traffic, making
       it harder for attackers to intercept and manipulate DNS queries.
"""
      
       dns_exfiltration_label.config(text=protections_text)

    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="DNS Exfiltration Server",command=lambda:DNS_exfiltration_server(new_window))
    button_in_new_window.pack()

    ip_label = tk.Label(new_window, text="Enter IP:")
    ip_label.pack()
    ip_entry = tk.Entry(new_window, width=50)
    ip_entry.pack()
    
    site_label = tk.Label(new_window, text="Enter Site:")
    site_label.pack()
    site_entry = tk.Entry(new_window, width=50)
    site_entry.pack()
    
    
    message_label = tk.Label(new_window, text="Enter Message:")
    message_label.pack()
    message_entry = tk.Entry(new_window, width=50)
    message_entry.pack()
    
    port_label = tk.Label(new_window, text="Enter Port:")
    port_label.pack()
    port_entry = tk.Entry(new_window, width=50)
    port_entry.pack()



    button_in_new_window = tk.Button(new_window, text="DNS Exfiltration Client",command=lambda:DNS_exfiltration_client(new_window,ip_entry.get(),site_entry.get(),message_entry.get(),port_entry.get()))
    button_in_new_window.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    dns_exfiltration_button = tk.Button(new_window, text="DNS Exfiltration Protections", command=display_dns_exfiltration_protections)
    dns_exfiltration_button.pack()

    # Create a label to display the protections 
    dns_exfiltration_label = tk.Label(new_window, text="", justify="left")
    dns_exfiltration_label.pack()
#open a new window when i click button for non app layer protocol
def open_new_window7():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="Non app layer protocol",font=title_font)
    label.pack()
    
    description_text = "The provided tool facilitates data exfiltration by encoding data into DNS queries and sending \nthem to a specified IP address. It breaks the data into chunks, encodes them in base64, and \ntransmits them via DNS requests. The receiving server decodes the data from these \nrequests, exploiting DNS for covert data transfer."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_non_app_layer_protections():
       protections_text = """
    Protections against Non application layer protocol attack:

        1. DNS Traffic Monitoring and Analysis:
           Monitor DNS Queries: Regularly monitor DNS queries for suspicious or abnormal patterns, such as unusually high numbers of queries to unusual or unknown domains.
           DNS Query Length: Implement controls to detect and alert on unusually long DNS queries which might indicate data exfiltration.
           DNS Response Size: Monitor and control the size of DNS responses to prevent large data transfers.
           
        2. DNS Filtering and Whitelisting:
           Domain Whitelisting: Implement domain whitelisting to allow DNS queries only to known and trusted domains.
           Reputation-based Filtering: Use reputation-based filtering to block DNS queries to known malicious or suspicious domains.
           
        3. Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS):
           Signature-based Detection: Use IDS/IPS with signatures to detect known patterns of DNS-based data exfiltration.
           Anomaly-based Detection: Implement anomaly-based detection systems that can identify unusual DNS traffic patterns.
           
        4. Endpoint Protection:
           Anti-malware Solutions: Ensure that all endpoints have up-to-date anti-malware solutions that can detect and prevent the execution of malicious scripts.
           Endpoint Detection and Response (EDR): Deploy EDR solutions that can provide real-time monitoring and response capabilities for suspicious activities on endpoints.
           
        5. Network Segmentation:
           Isolate Critical Systems: Implement network segmentation to isolate critical systems from those that are more exposed to potential threats. This limits the ability of an attacker to reach sensitive data.
           Control Internal DNS Resolution: Use internal DNS servers and restrict the ability of endpoints to directly query external DNS servers.
"""
      
       non_app_layer_protocol_label.config(text=protections_text)
    #Create a button in the new widow
    #for protocol tunneling server
    button_in_new_window = tk.Button(new_window, text="Non app layer protocol Server",command=lambda:non_app_layer_protocol_server(new_window,client_finished_event))
    button_in_new_window.pack()
    
    ip_label = tk.Label(new_window, text="Enter IP:")
    ip_label.pack()
    ip_entry = tk.Entry(new_window, width=50)
    ip_entry.pack()
    
    data_label = tk.Label(new_window, text="Enter message:")
    data_label.pack()
    data_entry = tk.Entry(new_window, width=50)
    data_entry.pack()
    client_finished_event = threading.Event()
    #for protocol tunneling client
    button_in_new_window = tk.Button(new_window, text="Non app layer protocol Client",command=lambda:non_app_layer_protocol_client(new_window,ip_entry.get(),data_entry.get(),client_finished_event))
    button_in_new_window.pack()
    #Open a new window when i click button for network sniffing
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    non_app_layer_protocol_button = tk.Button(new_window, text="Non application layer protocol Protections", command=display_non_app_layer_protections)
    non_app_layer_protocol_button.pack()

    # Create a label to display the protections 
    non_app_layer_protocol_label= tk.Label(new_window, text="", justify="left")
    non_app_layer_protocol_label.pack()
#Open a new window when i click button for data encryption/decryption    
def open_new_window8():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="Encryption/Decryption", font=("Helvetica", 16, "bold"))
    label.pack()

    description_text = "\nThis pair of scripts implements a basic file encryption and decryption system using AES \nencryption in Python. The encryption script encrypts files in a specified directory with a \ngiven extension, while the decryption script decrypts these encrypted files. The encryption \nscript takes a key and a directory as command-line arguments, encrypts each file in the \ndirectory with the specified extension, and appends .encrypted to the filenames. \nConversely, the decryption script requires the same key and directory to decrypt the \nencrypted files, removing the .encrypted extension to restore the original files. This \nsetup provides a straightforward solution for encrypting and decrypting files, enhancing \ntheir security during storage or transmission."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_encrypt_decrypt_protections():
       protections_text = """
       Encryption Benefits:
       
       1. Data Confidentiality:
             - Encryption ensures that only authorized parties can access the information. 
               This prevents unauthorized users from reading sensitive data, even if they manage to intercept it.
       2. Data Integrity:
             - Encryption helps in maintaining data integrity. It ensures that the data has not been altered during transmission
               or storage. Any tampering can be detected through checksums or hash functions used alongside encryption.
       3. Data Security:
             - Encryption protects data at rest and in transit. This is crucial for preventing data breaches and 
               protecting personal and financial information from cyberattacks.
       4. Authentication:
             - Encryption methods, like digital signatures, help in verifying the authenticity of data and the identity 
               of the sender. This ensures that the data is from a legitimate source.
       5. Privacy Protection:
             - Encryption safeguards individuals' privacy by ensuring that personal data is not accessible to unauthorized parties.
             This is particularly important in communication applications like messaging services.
       """
       encrypt_decrypt_label.config(text=protections_text)
    # Function to browse directory
    def browse_directory():
        directory = filedialog.askdirectory()
        directory_entry.delete(0, tk.END)  # Clear previous entry
        directory_entry.insert(0, directory)

    # Label and entry field for encryption key
    key_label = tk.Label(new_window, text="Encryption Key:")
    key_label.pack()
    key_entry = tk.Entry(new_window)
    key_entry.pack()

    # Label and entry field for directory
    directory_label = tk.Label(new_window, text="Directory:")
    directory_label.pack()
    directory_entry = tk.Entry(new_window)
    directory_entry.pack()

    # Button to browse directory
    browse_button = tk.Button(new_window, text="Browse", command=browse_directory)
    browse_button.pack()

    # Label and entry field for file extension
    ext_label = tk.Label(new_window, text="File Extension:")
    ext_label.pack()
    ext_entry = tk.Entry(new_window)
    ext_entry.pack()
    ext_entry.insert(0, ".docx")

    # Buttons to execute encryption and decryption
    encrypt_button = tk.Button(new_window, text="Encrypt Data", command=lambda: encrypt_data(new_window, key_entry.get(), directory_entry.get(), ext_entry.get()))
    encrypt_button.pack()

    decrypt_button = tk.Button(new_window, text="Decrypt Data", command=lambda: decrypt_data(new_window, key_entry.get(), directory_entry.get()))
    decrypt_button.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    
    encrypt_decrypt_button = tk.Button(new_window, text="Encryption Benefits", command=display_encrypt_decrypt_protections)
    encrypt_decrypt_button.pack()

    # Create a label to display the protections against network sniffing
    encrypt_decrypt_label = tk.Label(new_window, text="", justify="left")
    encrypt_decrypt_label.pack()  
#Open a new window when i click button for decoy content    
def open_new_window9():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="Decoy content", font=title_font)
    label.pack()
   
    description_text = "This tool is designed to verify the timestamps of files listed in a decoys.txt file. Each line in \nthe decoys.txt file contains the filename along with its creation, modification, and access \ntimestamps. The script reads this file, extracts the timestamps for each listed file, and \ncompares them with the actual timestamps retrieved from the file system. If any of the \ntimestamps do not match, indicating potential tampering, the script alerts the user. This \ntool serves as a simple integrity check for files by ensuring their timestamps align with the \nexpected values provided in the decoys.txt file."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_decoy_content_protections():
       protections_text = """
       Benefits:
       
       1. Detection of Unauthorized Changes:
                 -  Integrity Monitoring: By comparing the current timestamps of files with expected values, the tool can
                    detect any unauthorized changes, indicating potential tampering or security breaches.
       2. Security Auditing:
                 - Regular Checks: The tool can be scheduled to run at regular intervals, ensuring ongoing monitoring of 
                   critical files. This helps maintain a secure environment by promptly identifying suspicious activities.
       3. Incident Response and Forensic Analysis:
                 - Timeline Reconstruction: In the event of a security incident, the tool can help reconstruct a timeline of
                   when files were accessed, modified, or created. This information is crucial for forensic investigations and
                   understanding the scope of an attack.
       4. Compliance and Regulatory Requirements:
                 - Data Protection: Many regulations require organizations to implement measures to protect data integrity. 
                   This tool helps meet those requirements by providing a mechanism to monitor and verify file integrity.
                 - Audit Trails: It creates an audit trail of file access and modifications, which is often required for 
                   compliance with standards like GDPR, HIPAA, and PCI-DSS.
       5. Proactive Defense:
                 - Early Detection: By identifying changes to files promptly, the tool enables early detection of potential 
                   security threats. This allows for quicker responses and mitigation actions to prevent further damage.
       6. Operational Assurance
                 - System Reliability: Ensuring that critical system files remain unchanged unless intentionally modified helps 
                   maintain the reliability and stability of systems. This is essential for mission-critical applications and services.
                 - Change Management: The tool can be integrated into change management processes to verify 
                   that only authorized changes are made to system files.
       """
       decoy_content_label.config(text=protections_text)

    def browse_file():
        file = filedialog.askopenfilename()
        file_entry.delete(0, tk.END)  # Clear previous entry
        file_entry.insert(0, file) 
        
    file_label = tk.Label(new_window, text="file")
    file_label.pack()
    file_entry = tk.Entry(new_window)
    file_entry.pack()

    # Button to browse directory
    browse_button = tk.Button(new_window, text="Browse", command=browse_file)
    browse_button.pack()
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: decoy_content(new_window,file_entry.get()))
    button_in_new_window.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    
    decoy_content_button = tk.Button(new_window, text="Benefits", command=display_decoy_content_protections)
    decoy_content_button.pack()

    # Create a label to display the protections against network sniffing
    decoy_content_label = tk.Label(new_window, text="", justify="left")
    decoy_content_label.pack()  
#Open a new window when i click button for Burn in    
def open_new_window10():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="Burn in", font=title_font)
    label.pack()
    
    description_text = "This tool simulates a browsing session by making requests to random URLs retrieved from a \nspecified file. The user can adjust the clickthrough probability and set a maximum sleep \ntime between requests. The script reads URLs from the provided file and repeatedly makes \nrequests to random URLs based on the defined clickthrough probability. After each \nrequest, it waits for a random period within the specified sleep time before proceeding to \nthe next request. This tool can be used to simulate user behavior on websites or test web \nserver performance under varying loads."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_burn_in_protections():
       protections_text = """
       Benefits:
       Load Testing and Performance Monitoring:
       Benefit: Simulates user traffic to test the load handling capabilities and performance of web servers.
       Protection: Use tools like Apache JMeter or LoadRunner, which are designed for safe load testing with built-in safety measures.
       
       Automated Monitoring:
       Benefit: Regularly checks the availability and response status of websites to ensure they are up and running.
       Protection: Use dedicated monitoring services like Pingdom or UptimeRobot that respect site policies and have minimal impact.

       Potential Malicious Uses and Their Protections:
       
       Denial of Service (DoS) Attack:
       Issue: High volume of requests can overwhelm a web server, leading to a denial of service.
       Protection:
       Rate Limiting: Implement rate limiting on the server to control the number of requests from a single IP address.
       Firewalls: Use web application firewalls (WAFs) to detect and block malicious traffic patterns.
       DDoS Protection Services: Services like Cloudflare and AWS Shield can protect against distributed denial of service attacks.
       
       Click Fraud:
       Issue: Generating artificial traffic to manipulate ad click rates or website traffic statistics.
       Protection:
       Fraud Detection Systems: Implement systems to detect unusual traffic patterns indicative of click fraud.
       Ad Verification Services: Use third-party ad verification services to ensure the authenticity of clicks and impressions.
       """
       burn_in_label.config(text=protections_text)
       
    def browse_file():
        file = filedialog.askopenfilename()
        file_entry.delete(0, tk.END)  # Clear previous entry
        file_entry.insert(0, file) 
    
    file_label = tk.Label(new_window, text="file")
    file_label.pack()
    file_entry = tk.Entry(new_window)
    file_entry.pack()
    
    clickthrough_label = tk.Label(new_window, text="Enter Clickthrough:")
    clickthrough_label.pack()
    clickthrough_entry = tk.Entry(new_window)
    clickthrough_entry.pack()
    
    sleeptime_label = tk.Label(new_window, text="Enter Sleeptime:")
    sleeptime_label.pack()
    sleeptime_entry = tk.Entry(new_window)
    sleeptime_entry.pack()

    # Button to browse directory
    browse_button = tk.Button(new_window, text="Browse", command=browse_file)
    browse_button.pack()

    # Create a button to start the burn-in
    button_in_new_window = tk.Button(new_window, text="Start now", command=lambda: burn_in(
        new_window,
        file_entry.get(),
        clickthrough_entry.get(),
        sleeptime_entry.get()
    ))
    button_in_new_window.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    
    burn_in_button = tk.Button(new_window, text="Benefits", command=display_burn_in_protections)
    burn_in_button.pack()

    # Create a label to display the protections against network sniffing
    burn_in_label = tk.Label(new_window, text="", justify="left")
    burn_in_label.pack()
#Open a new window when i click button for Network Monitoring  
def open_new_window11():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="Network Monitoring",font=title_font)
    label.pack()
    
    description_text = "This tool is a powerful tool for analyzing network flows within a pcap file. It employs the \nscapy library to process packets, extracting crucial information from the IP layer. By \ncalculating packet lengths and organizing data into flow records based on source and \ndestination IP addresses, it effectively summarizes communication patterns between hosts. \nIts output, detailing byte counts for each pair of IP addresses, offers valuable insights into \nnetwork traffic behavior. This script proves instrumental for network administrators and \nsecurity analysts in understanding and assessing network activity captured in pcap files."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_network_monitering_protections():
       protections_text = """
       Protections Against Network Monitering
       1. Access Controls:
          - Role-Based Access Control (RBAC): Implement RBAC to ensure that only authorized personnel can access network monitoring tools and pcap files.
          - Multi-Factor Authentication (MFA): Use MFA for accessing network management systems to add an extra layer of security.
       2. Network Segmentation:
          - Segment Network Traffic: Divide the network into segments based on sensitivity and function. Limit access to sensitive segments to only those who need it.
          - VLANs and Firewalls: Use VLANs and firewalls to control and monitor traffic between network segments.
       3. Encryption:
          - Encrypt Traffic: Use strong encryption protocols like TLS for data in transit to protect it from being intercepted and analyzed.
          - VPNs: Use Virtual Private Networks (VPNs) for secure remote access to the network.
       4. Logging and Monitoring:
          - Activity Logs: Maintain detailed logs of access to network analysis tools and pcap files. Monitor these logs for suspicious activity.
          - Intrusion Detection Systems (IDS): Deploy IDS to detect unauthorized access or anomalies in network traffic.
       5. Network Security Policies:
          - Acceptable Use Policy: Develop and enforce a policy that defines acceptable use of network analysis tools.
          - Incident Response Plan: Have a plan in place to respond to incidents of unauthorized access or data breaches.
       6. User Training and Awareness:
          - Security Training: Regularly train employees on the importance of network security and the proper use of network analysis tools.
          - Awareness Programs: Conduct awareness programs to highlight the risks associated with unauthorized network traffic analysis.
       7. Tool-Specific Protections
          - Tool Access Restrictions: Restrict access to network analysis tools to specific machines or IP addresses.
          - Audit Trails: Implement audit trails to track the use of network analysis tools, including who used them, when, and for what purpose.
       8. Data Masking and Anonymization
          - Mask Sensitive Data: Mask or anonymize sensitive data within pcap files to protect privacy while still allowing for analysis.
          - Redact Data: Remove or redact personally identifiable information (PII) and other sensitive information from pcap files before analysis.
          """
       network_monitering_label.config(text=protections_text)
    def browse_file():
        file = filedialog.askopenfilename()
        file_entry.delete(0, tk.END)  # Clear previous entry
        file_entry.insert(0, file) 
    
    file_label = tk.Label(new_window, text="file")
    file_label.pack()
    file_entry = tk.Entry(new_window)
    file_entry.pack()
    browse_button = tk.Button(new_window, text="Browse", command=browse_file)
    browse_button.pack()
    
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: network_monitoring(new_window,file_entry.get()))
    button_in_new_window.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    
    network_monitering_button = tk.Button(new_window, text="Benefits", command=display_network_monitering_protections)
    network_monitering_button.pack()

    # Create a label to display the protections against network sniffing
    network_monitering_label = tk.Label(new_window, text="", justify="left")
    network_monitering_label.pack()
#Open a new window when i click button for Behavioral Analysis 
def open_new_window12():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="Behavioral Analysis",font=title_font)
    label.pack()
    
    description_text = "This tool monitors network connections established by processes on a system using the \npsutil library. Initially, it establishes a baseline of processes with network connections. Then, \nit continuously checks for changes in connection status and alerts the user if deviations \nfrom the baseline exceed a predefined threshold. This tool provides insights into process \nbehavior and helps detect suspicious network activity."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_behavioral_analysis_protections():
       protections_text = """
       Protections Against Behavioral Analysis:
       
       1. Access Controls:
          - Role-Based Access Control (RBAC): Ensure that only authorized personnel have access to behavioral analysis tools.
            Assign roles based on the principle of least privilege.
          - Multi-Factor Authentication (MFA): Implement MFA for accessing the systems where the behavioral analysis tools are deployed.
          
       2. Data Anonymization and Masking:
          - Anonymize Data: Remove or mask personally identifiable information (PII) from the data being analyzed to protect user privacy.
          - Use Aggregated Data: Where possible, use aggregated data to perform analysis instead of raw data that may contain sensitive information.

       3. Encryption:
          - Encrypt Data at Rest: Ensure that all data collected by the behavioral analysis tools is encrypted when stored.
          - Encrypt Data in Transit: Use strong encryption protocols like TLS to protect data being transmitted over the network.
 
       4. Logging and Monitoring:
          - Activity Logs: Keep detailed logs of who accessed the behavioral analysis tools, what data was accessed, and any changes made.
            Review these logs regularly for signs of misuse.
          - Real-Time Monitoring: Implement real-time monitoring to detect and respond to any unauthorized access or suspicious activities promptly.

       5. Policy and Compliance:
          - Develop Policies: Create clear policies regarding the use of behavioral analysis tools, specifying what is acceptable and what is not.
          - Regular Audits: Conduct regular audits to ensure compliance with policies and to identify any potential misuse.

       6. User Awareness and Training:
          - Training Programs: Conduct regular training sessions for employees on the ethical use of behavioral analysis tools and the importance of protecting privacy.
          - Awareness Campaigns: Run awareness campaigns to educate users about the risks associated with misuse and the importance of adhering to security policies.

       7. Technical Safeguards:
          - Network Segmentation: Isolate the systems running behavioral analysis tools from other critical systems to limit the impact of any potential misuse.
          - Rate Limiting: Implement rate limiting to prevent excessive data collection and to mitigate the risk of data exfiltration.
          - Intrusion Detection and Prevention Systems (IDPS): Deploy IDPS to monitor network traffic and detect any abnormal behavior that might indicate misuse of the analysis tools.

       """
       behavioral_analysis_label.config(text=protections_text)
    threshold_label = tk.Label(new_window, text="Threshold")
    threshold_label.pack()
    threshold_entry = tk.Entry(new_window)
    threshold_entry.pack()
    time_label = tk.Label(new_window, text="Baseline Time")
    time_label.pack()
    time_entry = tk.Entry(new_window)
    time_entry.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: behavioral_analysis(new_window,threshold_entry.get(),time_entry.get()))
    button_in_new_window.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    behavioral_analysis_button = tk.Button(new_window, text="Protections Against Behavioral Analysis", command=display_behavioral_analysis_protections)
    behavioral_analysis_button.pack()

    # Create a label to display the protections against network sniffing
    behavioral_analysis_label = tk.Label(new_window, text="", justify="left")
    behavioral_analysis_label.pack()  
#Open a new window when i click button for local email account
def open_new_window13():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="local email account",font=title_font)
    label.pack()
    
    description_text = "This tool processes an Outlook PST file, extracting information from each message within \nthe file. It imports the argparse module to parse command-line arguments. The \nprocess_archive function opens the specified PST file using the PffArchive class from the \nlibratom library and iterates through its folders. For each folder containing messages, it \nretrieves details such as sender name, subject, and plain text body of each message, \nprinting them to the console. In the main block, the script parses the command-line \nargument specifying the PST file path and calls the process_archive function to execute \nthe processing. This tool facilitates the extraction of email data from Outlook PST files for \nanalysis or archival purposes."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_local_email_protections():
       protections_text = """
       To Defend Against Such Attacks:
       
       1. File Access Control:

          - Ensure that sensitive files like PST files are protected by appropriate access controls.
          - Use file permissions to restrict access to authorized users only.
      
       2. Encryption:

          _ Encrypt PST files and other sensitive data. This ensures that even if the files are 
            accessed without authorization, the data within them remains protected.
       3. Endpoint Security:

          - Install and maintain up-to-date antivirus and anti-malware software on all 
            endpoints to detect and prevent malicious scripts from running.
       4. Regular Audits:

          - Regularly audit file access logs to detect any unauthorized access attempts.
            This can help in identifying potential threats early.
       5. User Education:

          - Educate users about the importance of handling PST files securely. 
            Ensure they understand not to share sensitive files and to report any suspicious activity.
       6. Software Updates:

          - Keep all software, including operating systems and email clients, updated with the latest security patches.
       """
       local_email_label.config(text=protections_text)
    def browse_file():
        file = filedialog.askopenfilename()
        file_entry.delete(0, tk.END)  # Clear previous entry
        file_entry.insert(0, file) 
    
    file_label = tk.Label(new_window, text="file")
    file_label.pack()
    file_entry = tk.Entry(new_window)
    file_entry.pack()
    browse_button = tk.Button(new_window, text="Browse", command=browse_file)
    browse_button.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: local_email_account(new_window,file_entry.get()))
    button_in_new_window.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    local_email_button = tk.Button(new_window, text="Protections Against Local Email Account Attack", command=display_local_email_protections)
    local_email_button.pack()

    # Create a label to display the protections against network sniffing
    local_email_label = tk.Label(new_window, text="", justify="left")
    local_email_label.pack()
#Open a new window when i click button for modify clipboard
def open_new_window14():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="Modify clipboard", font=title_font)
    label.pack()
    
    description_text = "This script provides a convenient method to replace sensitive information within clipboard \ndata on Windows systems. It utilizes win32clipboard for clipboard operations, re for regular \nexpression matching, and argparse for parsing command-line arguments. Upon detection \nof sensitive information in the clipboard, it replaces it with a custom value specified by the \nuser. The script runs continuously, monitoring the clipboard for changes, and terminates \nupon user interruption or encountering an error. This tool ensures privacy and security by \nallowing users to safeguard sensitive data before sharing or storing it."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_modify_clipboard_protections():
       protections_text = """
       To Defend Against Clipboard Attacks:
       
       1.Clipboard Monitoring and Restriction:
         - Implement software policies that restrict clipboard access.
           This can prevent unauthorized applications from reading or modifying clipboard data.
           
       2.Endpoint Security:
         - Ensure all endpoints have robust antivirus and anti-malware software installed.
         - These tools can detect and block malicious scripts attempting to access the clipboard.   
         
       3.Regular Audits:
         - Conduct regular audits of applications and scripts running on systems to ensure there are
           no unauthorized or malicious processes.  
           
       4.Limit Clipboard Access:
         - Configure operating system policies to limit clipboard access to trusted applications only. 
           On Windows, for example, this can be managed through group policies.
           
       5.Clipboard Management Tools:

         - Use clipboard management tools that can provide additional security features such as clipboard history and access control.
           Some of these tools can alert users when clipboard data is accessed or modified by an application.    
           
       6. Script Monitoring and Control:

         - Implement monitoring solutions to detect and alert on the execution of unauthorized scripts. Control script execution by using
           tools like AppLocker on Windows, which can enforce policies on which scripts can run.    
       """
       modify_clipboard_label.config(text=protections_text)
    sensitive_info_label = tk.Label(new_window, text="Select the type of sensitive information:")
    sensitive_info_label.pack()
    sensitive_info_var = tk.StringVar(new_window)
    sensitive_info_choices = ['email', 'phone', 'url', 'date', 'ip', 'credit_card', 'ssn']
    
    # Create a themed Combobox
    sensitive_info_combobox = ttk.Combobox(new_window, textvariable=sensitive_info_var, values=sensitive_info_choices, state="readonly")
    sensitive_info_combobox.pack()
    
    # Entry widget to enter replacement text
    replacement_label = tk.Label(new_window, text="Enter replacement text:")
    replacement_label.pack()
    replacement_entry = tk.Entry(new_window)
    replacement_entry.pack()
    
    # Create a button in the new window
    button_in_new_window = tk.Button(new_window, text="Start now", command=lambda: modify_clipboard(new_window, sensitive_info_var.get(), replacement_entry.get()))
    button_in_new_window.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")

    local_email_button = tk.Button(new_window, text="Protections Against Clipboard Attack", command=display_modify_clipboard_protections)
    local_email_button.pack()

    # Create a label to display the protections against network sniffing
    modify_clipboard_label = tk.Label(new_window, text="", justify="left")
    modify_clipboard_label.pack()
#Open a new window when i click button for user discovery
def open_new_window15():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="User Discovery",font=title_font)
    label.pack()
    
    description_text = "This tool utilizes the wmi module to gather information about user accounts and the \nWindows password policy on a system. It first retrieves a list of Administrator accounts by \nquerying the Win32_Group class and filtering for the Administrators group. Then, it lists \nall user accounts on the device using the Win32_UserAccount class, displaying various \nproperties such as username, administrator status, account status, and password policy \ndetails. Finally, it prints the Windows password policy by executing the command net \naccounts using os.system(). This tool provides administrators with comprehensive \ninsights into user accounts and password policies on a Windows system."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_user_discovery_protections():
       protections_text = """
       To Defend Against This Attacks:
       
       1. Monitoring and Logging:
          - Enable Detailed Logging:Enable and monitor detailed logging of WMI activity. Tools like Sysmon can help capture WMI queries
            and other system activities.
          _ Monitor Command Execution: Track the execution of commands and scripts, particularly those involving
            WMI and os.system calls.
          - PowerShell Logging: Enable PowerShell script block logging and transcription to capture and review executed commands.

       2. Restrict WMI Access:
          - WMI Permissions: Restrict WMI permissions to only those users and groups that require it. 
            Limit WMI access to specific administrative accounts.
          - Group Policy: Use Group Policy to configure WMI namespace permissions and restrict access.

       3. Endpoint Protection:
          - Application Whitelisting: Implement application whitelisting to control which scripts and executables can run on your systems.
          - Behavioral Analysis: Use endpoint security solutions that include behavioral analysis to detect and 
            block suspicious activity related to WMI and script execution.

       4. User and Account Security:
          - Regular Audits: Conduct regular audits of user accounts and group memberships to ensure only necessary accounts have administrative privileges.
          - Account Monitoring: Implement real-time monitoring and alerting for changes to user accounts and group memberships.

       5. Script and Command Execution Policies:
          - Execution Policy: Set restrictive execution policies for PowerShell and other scripting environments to prevent unauthorized script execution.
          - Restricted Admin Accounts: Use separate administrative accounts with limited access for daily tasks, and only use full administrative accounts when absolutely necessary.

       6. Password Policies and MFA:
          - Enforce Strong Password Policies: Implement strong password policies and ensure they are enforced across all user accounts.
          - Multi-Factor Authentication (MFA): Require MFA for all administrative accounts to add an additional layer of security.
     
       """
       user_discovery_label.config(text=protections_text)
       
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: user_discovery(new_window))
    button_in_new_window.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    user_discovery_button = tk.Button(new_window, text="Protections Against User Discovery Attack", command=display_user_discovery_protections)
    user_discovery_button.pack()

    # Create a label to display the protections against network sniffing
    user_discovery_label = tk.Label(new_window, text="", justify="left")
    user_discovery_label.pack()
#Open a new window when i click button for Account Access Removal
def open_new_window16():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x300")
    label = tk.Label(new_window, text="Account Access Removal", font=title_font)
    label.pack()

    description_text = "This tool facilitates changing user passwords on both Windows and Linux systems. It \nemploys platform detection to determine the operating system, then utilizes different \nmethods (setWindowsPassword for Windows and setLinuxPassword for Linux) to update \nthe password. Additionally, it includes a changeCriteria function to restrict password \nchanges for specific users, ensuring security measures. Users can input the computer \nname, username, and new password via command-line arguments. This tool streamlines \nthe process of password management, providing a convenient and platform-agnostic \nsolution for system administrators."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_account_access_protections():
       protections_text = """
       To Defend Against Account Access Removal Attacks:
       
       1.Access Control:
        - Restrict access to the script to authorized administrators only.
        - Use file permissions to limit who can read or execute the script.
       
       2.Authentication:
        - Require administrative credentials to run the script.
        - Implement multi-factor authentication (MFA) for added security.

       3.Logging:
        - Log all attempts to execute the script, including the username and timestamp.
        - Monitor logs regularly for suspicious activity.

       4.Encryption:
        - Store and transmit passwords securely using encryption.
        - Avoid hardcoding passwords within the script.

       5.Validation:
        - Add validation checks to ensure only authorized usernames and systems can have their passwords changed.
        - Ensure the new password meets strong password policies.

       """
       account_access_label.config(text=protections_text)
    # Input fields for computer, username, and password
    tk.Label(new_window, text="Computer:").pack()
    computer_entry = tk.Entry(new_window)
    computer_entry.pack()

    tk.Label(new_window, text="Username:").pack()
    username_entry = tk.Entry(new_window)
    username_entry.pack()

    tk.Label(new_window, text="New Password:").pack()
    password_entry = tk.Entry(new_window, show="*")
    password_entry.pack()

    # Create a button in the new window
    button_in_new_window = tk.Button(new_window, text="Start now", 
                                     command=lambda: access_removal(new_window, computer_entry.get(), username_entry.get(), password_entry.get()))
    button_in_new_window.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    account_access_button = tk.Button(new_window, text="Protections Against Local Email Account Attack", command=display_account_access_protections)
    account_access_button.pack()

    # Create a label to display the protections against network sniffing
    account_access_label = tk.Label(new_window, text="", justify="left")
    account_access_label.pack()
#Open a new window when i click button for Sys Activity Monitpring
def open_new_window17():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("400x400")
    event_id_descriptions = {
    4672: "Special privileges assigned to new logon.",
    4624: "An account was successfully logged on.",
    4634: "An account was logged off.",
    4648: "A logon was attempted using explicit credentials.",
    4768: "A Kerberos authentication ticket (TGT) was requested.",
    4771: "Kerberos pre-authentication failed.",
    4776: "The computer attempted to validate the credentials for an account.",
    4781: "The name of an account was changed.",
    4798: "A user's local group membership was enumerated."}
    label = tk.Label(new_window, text="Sys Activity Monitoring", font=title_font)
    label.pack()

    description_text = "This script is a handy tool for monitoring specific events in Windows event logs. It uses the \nwin32evtlog module to access event logs on a specified server, focusing on event ID \n4672, which signifies successful logins with administrative rights. Users can customize \nparameters such as the server name, log type, and event ID to tailor the monitoring \nprocess. Upon execution, the tool scans the event log for occurrences of the specified \nevent and reports any instances found, along with the associated user account and the \ncount of occurrences. This tool is beneficial for system administrators seeking to track \ncritical security events within their Windows environments efficiently."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_sys_monitoring_protections():
       protections_text = """
       To Defend Against Sys Activity Monitoring Attacks:
       
       1. Logging and Monitoring:
          - Implement logging for auditing purposes and to detect suspicious activities.
            Log every script execution attempt and its parameters.

       2. Role-Based Access Control (RBAC):
          - Ensure that only users with appropriate roles and permissions can execute scripts that access system logs.

       3. Use Secure Methods to Access Logs:
          - If possible, use secure methods to access logs, such as remote access with proper authentication and 
            encryption mechanisms.

       4. Network Security:
          - Ensure that the server where this script runs is secured within a trusted network environment.
            Use firewalls and network segmentation to limit access.

       5. Rate Limiting and Throttling:
          - Implement rate limiting to prevent brute force or repeated attempts to misuse the script.

       6. Alerting and Incident Response:
          - Set up alerts to notify administrators of unusual script execution or log access patterns. Have an incident response plan in place.

       """
       sys_monitoring_label.config(text=protections_text)
    # Server input
    server_label = tk.Label(new_window, text="Server:")
    server_label.pack()
    server_entry = tk.Entry(new_window)
    server_entry.pack()
    server_entry.insert(0, "localhost")  # default value

    # Logtype input
    logtype_label = tk.Label(new_window, text="Logtype:")
    logtype_label.pack()
    logtype_entry = tk.Entry(new_window)
    logtype_entry.pack()
    logtype_entry.insert(0, "Security")  # default value

    # Event ID selection
    event_id_label = tk.Label(new_window, text="Event ID:")
    event_id_label.pack()
    event_id_combobox = ttk.Combobox(new_window, values=list(event_id_descriptions.keys()))
    event_id_combobox.pack()
    event_id_combobox.set(4672)  # default value

    # Create a button in the new window
    button_in_new_window = tk.Button(new_window, text="Start now",
                                     command=lambda: sys_activity_monitoring(new_window, server_entry.get(), logtype_entry.get(), event_id_combobox.get()))
    button_in_new_window.pack()
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    canvas.create_line(0, 1, 580, 1, fill="black")
    sys_monitoring_button = tk.Button(new_window, text="Protections Against Sys Activity Monitoring Attack", command=display_sys_monitoring_protections)
    sys_monitoring_button.pack()

    # Create a label to display the protections against network sniffing
    sys_monitoring_label = tk.Label(new_window, text="", justify="left")
    sys_monitoring_label.pack()
#Open a new window when i click button for port scanning
def open_new_window18():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("600x400")
    
    # Title label
    title_font = font.Font(family='Helvetica', size=16, weight='bold')
    label = tk.Label(new_window, text="Port Scanner", font=title_font)
    label.pack(pady=10)
    
    description_text = "This tool offers a straightforward port scanning utility in Python. It allows users to scan ports \non a target host to determine whether they are open or closed. The tool begins by \npresenting a list of well-known ports and their descriptions. Then, it prompts users to \nspecify the target host as a command-line argument. After parsing the arguments, it \ninitiates the port scanning process on the specified target host, examining each well-\nknown port and reporting its status. This tool is useful for network administrators and \nsecurity analysts seeking to assess the security status of a target system quickly."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_port_scanning_protections():
       protections_text = """
       To Defend Against Port Scanning:
       
       1. Firewalls:  
          - Configure Firewalls Properly: Use firewalls to block unnecessary ports.
            Only open ports that are absolutely necessary for your operations.
          - Implement Stateful Inspection: Firewalls with stateful inspection can track the  
            state of active connections and make decisions based on the context of the traffic.
       2. Intrusion Detection and Prevention Systems (IDS/IPS):
          - Deploy IDS/IPS: These systems can detect and potentially block port scanning activities. 
            They analyze network traffic for suspicious patterns that match known scanning techniques.
          - Snort: An open-source IDS/IPS that can be configured to detect port scans.
       3. Network Segmentation:
          - Segment Your Network: Isolate sensitive systems and services from the rest of the network.
            This limits the damage an attacker can do if they manage to penetrate your network.
          - DMZ (Demilitarized Zone): Place public-facing services in a DMZ to separate them from your internal network.
       4. Rate Limiting and Throttling:
          - Implement Rate Limiting: Limit the number of connection attempts from a single IP address over a specified period.
          - Honeypots: Deploy honeypots to detect and analyze scanning activities.
            Honeypots can attract attackers, making it easier to study their methods and prepare defenses.
       5. Regular Monitoring and Logging:
          - Log Analysis: Regularly review logs for unusual activity, such as repeated connection attempts to various ports.
          - SIEM (Security Information and Event Management): Use SIEM solutions to aggregate and analyze logs from
            various sources
       7. Network Obfuscation:
          - Port Knocking: This technique involves requiring a sequence of port access attempts before opening a port for connection. 
            It hides services from casual port scans.
          - Moving Target Defense: Dynamically change the IP addresses and ports of services to make it harder for attackers to target them.
       """
       port_scanning_label.config(text=protections_text)
    # Host entry label and field
    host_label = tk.Label(new_window, text="Enter Host:")
    host_label.pack()
    host_entry = tk.Entry(new_window, width=50)
    host_entry.pack(pady=5)
    
    # Create a button in the new window to start the scan
    button_in_new_window = tk.Button(new_window, text="Start Scan", command=lambda: port_scanner(new_window, host_entry.get()))
    button_in_new_window.pack(pady=10)
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    port_scanning_button = tk.Button(new_window, text="Protections Against Port Scanning", command=display_port_scanning_protections)
    port_scanning_button.pack()

    # Create a label to display the protections against network sniffing
    port_scanning_label = tk.Label(new_window, text="", justify="left")
    port_scanning_label.pack()
#Open a new window when i click button for os detection   
def open_new_window19():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("500x400")
    
    # Title label
    title_font = font.Font(family='Helvetica', size=16, weight='bold')
    label = tk.Label(new_window, text="OS Detection", font=title_font)
    label.pack(pady=10)
    
    description_text = "This tool utilizes Scapy, a powerful packet manipulation tool, to detect the operating system \nof a target host based on Time-To-Live (TTL) values in ICMP packets. It defines a \ndetect_os function that sends an ICMP packet to the target host and examines the TTL \nvalue in the response. Based on the TTL value, it infers the operating system as Linux if \nTTL is less than or equal to 64, Windows if TTL is greater than 64, and Unknown \notherwise. Upon execution, the script prompts users to specify the target IP address as a \ncommand-line argument. It then initiates the OS detection process on the specified target \nand reports the detected operating system. This tool is valuable for network \nadministrators and security analysts to identify the operating system of target hosts \nquickly and accurately."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    def display_os_detection_protections():
       protections_text = """
       To Defend Against OS Detection:
       
       1. Network-Level Protections:
          - Firewalls and Intrusion Detection Systems (IDS)
            Firewalls: Configure your firewall to drop or modify packets that attempt to probe your system.
            IDS: Deploy an intrusion detection system that can detect and block OS fingerprinting attempts.
          - Packet Scrubbing
            Packet Scrubbers: Use packet scrubbing tools to modify or remove OS-specific signatures from outgoing packets.
       2. Obfuscation Techniques:
          - TCP/IP Stack Fingerprint Alteration
            Change TCP/IP Stack Parameters: Modify parameters such as TCP sequence numbers, window
            sizes, and timestamps to obscure your OS fingerprint.
            Tools: Utilize tools or settings in your OS to alter these parameters (e.g., sysctl settings in Linux).         
       3. Host-Based Protections:
          - System Hardening
            Regular Updates: Keep your system and applications updated to avoid vulnerabilities that 
            could be exploited for OS detection.
            Security Patches: Apply security patches promptly to mitigate known exploits
            
       4. Proxy Servers and VPNs:
          - Proxy Servers: Can modify TTL values as packets pass through them, providing an additional layer of obfuscation.
          - VPN Services: VPNs typically alter the TTL values, as packets are routed through a different 
            network, masking the original TTL values.
       """
       os_detection_label.config(text=protections_text)   
    # Target IP entry
    ip_label = Label(new_window, text="Enter Target IP:")
    ip_label.pack()
    ip_entry = Entry(new_window, width=50)
    ip_entry.pack(pady=5)
    
    # Button to start detection
    button_in_new_window = Button(new_window, text="Start Detection", command=lambda: os_detection(new_window, ip_entry.get()))
    button_in_new_window.pack(pady=10)
    

    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")
    
    os_detection_button = tk.Button(new_window, text="Protections Against OS Detection", command=display_os_detection_protections)
    os_detection_button.pack()

    # Create a label to display the protections against network sniffing
    os_detection_label = tk.Label(new_window, text="", justify="left")
    os_detection_label.pack()
#Open a new window when i click button for network device discovery   
def open_new_window20():
    new_window = tk.Toplevel(root)
    new_window.title("Rajeh")
    new_window.geometry("500x400")
    
    # Title label
    title_font = font.Font(family='Helvetica', size=16, weight='bold')
    label = tk.Label(new_window, text="Network Device Discovery", font=title_font)
    label.pack(pady=10)
    
    description_text = "This script utilizes Scapy and the termcolor module to perform an ARP scan on a target IP \naddress or range. It defines a scan function to send ARP requests to the target IP(s) and \nretrieve responses containing IP-MAC address pairs. The print_result function formats and \nprints the discovered devices' IP and MAC addresses. Upon execution, users can specify \nthe target IP address or range as a command-line argument, with an optional timeout \nvalue for ARP requests. The script then performs the ARP scan, displaying the discovered \ndevices' details or indicating if no devices are found. This tool is helpful for network \nadministrators to quickly identify active devices on a network."
    description_label = Label(new_window, text=description_text, justify="left")
    description_label.pack(pady=10)
    
    def display_device_discovery_protections():
       protections_text = """
       To Defend Against Device Discovery:
       
       1. Firewall Configuration
          - Personal Firewall:
            Enable Firewall: Ensure the firewall is enabled on all devices.
            Windows: Enable Windows Defender Firewall.
            MacOS: Enable the built-in firewall.
            Linux: Use iptables or firewalld.
          - Block ICMP Requests:
            Block Ping: Configure the firewall to block ICMP echo requests (ping), which are commonly used for network discovery.
            
       2. Static ARP Entries
          - Static ARP Tables: Configure static ARP entries on your devices to prevent ARP spoofing and limit the response to ARP requests.
          - Windows: Use the arp -s command to set static ARP entries.
          - Linux/MacOS: Use the arp or ip neighbor add command to set static ARP entries.     
          
       3. MAC Address Filtering
          - MAC Filtering: Configure MAC address filtering on your router or switch to allow only known devices to connect to the network.   
      
       4.Use Secure Network Protocols
          - Secure Protocols: Use secure protocols like IPv6, which has built-in security features that
            can help mitigate some ARP-related issues present in IPv4.   
         """
       device_discovery_label.config(text=protections_text)   
     # Timeout entry
    timeout_label = Label(new_window, text="Enter Timeout (seconds):")
    timeout_label.pack()
    timeout_entry = Entry(new_window, width=10)
    timeout_entry.pack(pady=5)
    
    # IP range entry
    ip_label = Label(new_window, text="Enter IP Range:")
    ip_label.pack()
    ip_entry = Entry(new_window, width=50)
    ip_entry.pack(pady=5)
    
    # Button to start discovery
    button_in_new_window = Button(new_window, text="Start Discovery", command=lambda: network_device_discovery(new_window, ip_entry.get(),timeout_entry.get()))
    button_in_new_window.pack(pady=10)
    
    canvas = tk.Canvas(new_window, width=580, height=2, bg="gray")
    canvas.pack(pady=20)
    canvas.create_line(0, 1, 580, 1, fill="black")

    device_discovery_button = tk.Button(new_window, text="Protections Against Network Device Discovery", command=display_device_discovery_protections)
    device_discovery_button.pack()

    # Create a label to display the protections against network sniffing
    device_discovery_label = tk.Label(new_window, text="", justify="left")
    device_discovery_label.pack()


















#Create the network Sniffing button
network_sniffing=Button(root,text="Network Sniffing",command=open_new_window1,padx=40,pady=30).grid(row=6,column=5,padx=50,pady=50)
#Create the  File and Directory Discovery button
file_and_directory_discovery=Button(root,text="File & Directory Discovery",command=open_new_window2,padx=40,pady=30).grid(row=6,column=15,padx=50,pady=50)
#Create the remote services button
remot_services=Button(root,text="Remote Services",command=open_new_window3,padx=40,pady=30).grid(row=6,column=20,padx=50,pady=50)
#Create the encrypted channel button
remot_services=Button(root,text="Encrypt Channel",command=open_new_window4,padx=40,pady=30).grid(row=6,column=23,padx=50,pady=50)
#Create the Protocol Tunneling button
remot_services=Button(root,text="Protocol Tunneling",command=open_new_window5,padx=40,pady=30).grid(row=6,column=25,padx=50,pady=50)
#Create the non app layer protocol button
remot_services=Button(root,text="Non application layer protocol",command=open_new_window7,padx=40,pady=30).grid(row=7,column=5,padx=50,pady=50)
#Create the data encryption button
remot_services=Button(root,text="Data Encryption/Decryption",command=open_new_window8,padx=40,pady=30).grid(row=7,column=15,padx=50,pady=50)
#Create the decoy content button
remot_services=Button(root,text="Decoy content",command=open_new_window9,padx=40,pady=30).grid(row=7,column=20,padx=50,pady=50)
#Create the Burn in button
remot_services=Button(root,text="Burn in",command=open_new_window10,padx=40,pady=30).grid(row=7,column=23,padx=50,pady=50)
#Create Network Monitoring button
remot_services=Button(root,text="Network Monitoring",command=open_new_window11,padx=40,pady=30).grid(row=7,column=25,padx=50,pady=50)
#Create Behavioral analysis button
remot_services=Button(root,text="Behavioral Analysis",command=open_new_window12,padx=40,pady=30).grid(row=9,column=5,padx=50,pady=50)
#Create localemailaccount button
remot_services=Button(root,text="local email account",command=open_new_window13,padx=40,pady=30).grid(row=9,column=15,padx=50,pady=50)
#Create modify clipboard button
remot_services=Button(root,text="Modify Clipboard",command=open_new_window14,padx=40,pady=30).grid(row=9,column=20,padx=50,pady=50)
#Create userdiscovery button
remot_services=Button(root,text="User Discovery",command=open_new_window15,padx=40,pady=30).grid(row=9,column=23,padx=50,pady=50)
#Create the DNS exfiltration button
remot_services=Button(root,text="DNS Exfiltration",command=open_new_window6,padx=40,pady=30).grid(row=9,column=25,padx=50,pady=50)
#Create the Acount Access Removal button
account_access_removal=Button(root,text="Account Access Removal",command=open_new_window16,padx=40,pady=30).grid(row=11,column=5,padx=50,pady=50)
#Create the Sys Activity Monitoring button
account_access_removal=Button(root,text="Sys Activity Monitoring",command=open_new_window17,padx=40,pady=30).grid(row=11,column=15,padx=50,pady=50)
#Create the port scanner button
account_access_removal=Button(root,text="Port Scanner",command=open_new_window18,padx=40,pady=30).grid(row=11,column=20,padx=50,pady=50)
#Create the os detection button
account_access_removal=Button(root,text="OS Detection",command=open_new_window19,padx=40,pady=30).grid(row=11,column=23,padx=50,pady=50)
#Create the network device discovery button
account_access_removal=Button(root,text="Network Device Discovery",command=open_new_window20,padx=40,pady=30).grid(row=11,column=25,padx=50,pady=50)







root.mainloop()


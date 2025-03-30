import subprocess
from tkinter import *
import tkinter as tk
from tkinter  import messagebox
import threading
from threading import Thread

root =Tk()

# Create a custom font with a larger size
title_font = ("Helvetica", 24)
#Create a label widget
#Title=Label(root,text="Network Security Scanner",font=title_font).grid(row=0,column=20)
root.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
root.title("AYMAN KANSO ULFG3")



#Running Network Sniffing script and display it
def sniffing_script(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\8.2_Network_Sniffing\NetworkCredentialSniffing.py"
    try:
        # Execute the script using subprocess and catch the output
        output= subprocess.check_output(['python', script_path], universal_newlines=True)
        
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, f"Error: {e}")
#Running File & Directory Discovery script and display it        
def discovery_script(new_window):
    script_path=r"C:\Users\user\Desktop\FYP\9.2_File_and_Directory_Discovery\FileDiscovery.py"
    try:
        # Execute the script using subprocess and catch the output
        output=subprocess.check_output(['python',script_path],universal_newlines=True)
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, f"Error: {e}")
#Running Network Sniffing script and display it
def remote_services_script(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\10.1_Remote_Services\RemoteServices.py"
    try:
        # Execute the script using subprocess and catch the output
        output= subprocess.check_output(['python', script_path], universal_newlines=True)
        
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, f"Error: {e}")       
#Running encrypted server script and display it        
def encrypted_channel_server(new_window):
    def run(new_window):    
        try:
            server_output_text = tk.Text(new_window, height=30, width=70)
            server_output_text.pack(padx=20,pady=20)
            server_output_text.config(state=tk.DISABLED)
            output = subprocess.check_output(['python', r'C:\Users\user\Desktop\FYP\12.1_Encrypted_Channel\EncryptedChannelServer.py'], universal_newlines=True)
            server_output_text.config(state=tk.NORMAL)
            server_output_text.delete(1.0, tk.END)
            server_output_text.insert(tk.END, output)
            server_output_text.config(state=tk.DISABLED)
        except subprocess.CalledProcessError as e:
            server_output_text.config(state=tk.NORMAL)
            server_output_text.delete(1.0, tk.END)
            server_output_text.insert(tk.END, f"Server Error: {e}")
            server_output_text.config(state=tk.DISABLED)
    
    # Run the server script in a separate thread
    server_thread = threading.Thread(target=lambda:run(new_window))
    server_thread.start()  
#Running encrypted client script and display it        
def encrypted_channel_client(new_window):
    def run(new_window):
        try:
            client_output_text = tk.Text(new_window, height=30, width=70)
            client_output_text.pack(padx=5, pady=20)
            client_output_text.config(state=tk.DISABLED)
            output = subprocess.check_output(['python', r'C:\Users\user\Desktop\FYP\12.1_Encrypted_Channel\EncryptedChannelClient.py'], universal_newlines=True)
            client_output_text.config(state=tk.NORMAL)
            client_output_text.delete(1.0, tk.END)
            client_output_text.insert(tk.END, output)
            client_output_text.config(state=tk.DISABLED)
        except subprocess.CalledProcessError as e:
            client_output_text.config(state=tk.NORMAL)
            client_output_text.delete(1.0, tk.END)
            client_output_text.insert(tk.END, f"Client Error: {e}")
            client_output_text.config(state=tk.DISABLED)
    
    # Run the client script in a separate thread
    client_thread = threading.Thread(target=run(new_window))
    client_thread.start() 
#Running protocol tunneling  script and display it     
def run_server(script_path):
    try:
        # Execute the script using subprocess and catch the output
        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        while True:
            output_line = process.stdout.readline()
            if not output_line:
                break
            # Update the GUI with the server output
            server_output_text.config(state=tk.NORMAL)
            server_output_text.insert(tk.END, output_line)
            server_output_text.see(tk.END)
            server_output_text.config(state=tk.DISABLED)
    except Exception as e:
        # Handle any errors that occur during script execution
        server_output_text.config(state=tk.NORMAL)
        server_output_text.delete(1.0, tk.END)
        server_output_text.insert(tk.END, f"Error: {e}")
        server_output_text.config(state=tk.DISABLED)
def update_output(output):
    client_output_text.config(state=tk.NORMAL)
    client_output_text.delete(1.0, tk.END)
    client_output_text.insert(tk.END, output)
    client_output_text.config(state=tk.DISABLED)
def protocol_tunneling_server(new_window):
    script_path=r"C:\Users\user\Desktop\FYP\12.2_Protocol_Tunneling\ProtocolTunnelingServer.py"
    global server_output_text
    server_output_text = Text(new_window, wrap=WORD, width=70, height=30)
    server_output_text.pack()
    server_output_text.config(state=tk.DISABLED)
    
    # Run the server function in a separate thread
    server_thread = threading.Thread(target=run_server, args=(script_path,))
    server_thread.start()
def protocol_tunneling_client(new_window):
    
    def run_client(script_path):
        try:
           # Execute the script using subprocess and catch the output
           output = subprocess.check_output(['python', script_path], universal_newlines=True)
        
           # Display the output in the Text widget
           new_window.after(0, lambda: update_output(output))
        except subprocess.CalledProcessError as e:
           # Handle any errors that occur during script execution
           new_window.after(0, lambda: update_output(f"Error: {e}"))
    script_path = r"C:\Users\user\Desktop\FYP\12.2_Protocol_Tunneling\ProtocolTunnelingClient.py"
    global client_output_text
    client_output_text = Text(new_window, wrap=WORD, width=70, height=30)
    client_output_text.pack()
    client_output_text.config(state=tk.DISABLED)
    
    # Run the client function in a separate thread
    client_thread = threading.Thread(target=run_client, args=(script_path,))
    client_thread.start()  
#Running DNS Exfiltrate script and display it
def run_server(script_path):
    try:
        # Execute the script using subprocess and catch the output
        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        while True:
            output_line = process.stdout.readline()
            if not output_line:
                break
            # Update the GUI with the server output
            server_output_text.config(state=tk.NORMAL)
            server_output_text.insert(tk.END, output_line)
            server_output_text.see(tk.END)
            server_output_text.config(state=tk.DISABLED)
    except Exception as e:
        # Handle any errors that occur during script execution
        server_output_text.config(state=tk.NORMAL)
        server_output_text.delete(1.0, tk.END)
        server_output_text.insert(tk.END, f"Error: {e}")
        server_output_text.config(state=tk.DISABLED)
def update_output(output):
    client_output_text.config(state=tk.NORMAL)
    client_output_text.delete(1.0, tk.END)
    client_output_text.insert(tk.END, output)
    client_output_text.config(state=tk.DISABLED)
def DNS_exfiltration_server(new_window):
    script_path=r"C:\Users\user\Desktop\FYP\13.1_Alternative_Protocol\DNSExfiltrationServer.py"
    global server_output_text
    server_output_text = Text(new_window, wrap=WORD, width=70, height=30)
    server_output_text.pack()
    server_output_text.config(state=tk.DISABLED)
    
    # Run the server function in a separate thread
    server_thread = threading.Thread(target=run_server, args=(script_path,))
    server_thread.start()
def DNS_exfiltration_client(new_window):
    
    def run_client(script_path):
        try:
           # Execute the script using subprocess and catch the output
           output = subprocess.check_output(['python', script_path], universal_newlines=True)
        
           # Display the output in the Text widget
           new_window.after(0, lambda: update_output(output))
        except subprocess.CalledProcessError as e:
           # Handle any errors that occur during script execution
           new_window.after(0, lambda: update_output(f"Error: {e}"))
    script_path = r"C:\Users\user\Desktop\FYP\13.1_Alternative_Protocol\DNSExfiltration.py"
    global client_output_text
    client_output_text = Text(new_window, wrap=WORD, width=70, height=30)
    client_output_text.pack()
    client_output_text.config(state=tk.DISABLED)
    
    # Run the client function in a separate thread
    client_thread = threading.Thread(target=run_client, args=(script_path,))
    client_thread.start()  
#Running non app server/client script and display it        
def run_server(script_path, server_output_text, client_finished_event):
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
            if not output_line:
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
def non_app_layer_protocol_server(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\13.2_Non-Application_Layer_Protocol\NonApplicationServer.py"
    server_output_text = Text(new_window, wrap=WORD, width=70, height=30)
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
def non_app_layer_protocol_client(new_window):
    
    def run_client(script_path):
        try:
            # Execute the script using subprocess and catch the output
            output = subprocess.check_output(['python', script_path], universal_newlines=True)
        
            # Display the output in the Text widget
            new_window.after(0, lambda: update_output(output))
        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during script execution
            new_window.after(0, lambda: update_output(f"Error: {e}"))
    
    script_path = r"C:\Users\user\Desktop\FYP\13.2_Non-Application_Layer_Protocol\NonApplicationClient.py"
    global client_output_text
    client_output_text = Text(new_window, wrap=WORD, width=70, height=30)
    client_output_text.pack()
    client_output_text.config(state=tk.DISABLED)
    
    # Run the client function in a separate thread
    client_thread = threading.Thread(target=run_client, args=(script_path,))
    client_thread.start()  
#Running data encryption script and display it    
def encrypt_data(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\14.1_Data_Encryption\DataEncryption.py"
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
        output_text.insert(END, f"Error: {e}")
#Running data decryption script and display it    
def decrypt_data(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\14.1_Data_Encryption\DataDecryption.py"
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
        output_text.insert(END, f"Error: {e}")
#Running Decoy content script and display it        
def decoy_content(new_window):
    script_path=r"C:\Users\user\Desktop\FYP\15.2_Decoy_Content\DecoyContent.py"
    try:
        # Execute the script using subprocess and catch the output
        output=subprocess.check_output(['python',script_path],universal_newlines=True)
        
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
def burn_in(new_window):
    def execute_script():
        script_path = r"C:\Users\user\Desktop\FYP\16.3_Burn_In\BurnIn.py"
        try:
            # Execute the script using subprocess and catch the output
            output = subprocess.check_output(['python', script_path], universal_newlines=True)
            
            # Update the Text widget with the output
            new_window.output_text.insert(END, output)
        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during script execution
            new_window.output_text.insert(END, f"Error: {e}")

    # Create a Text widget for displaying the output
    new_window.output_text = Text(new_window, wrap=WORD, width=70, height=30)
    new_window.output_text.pack()

    # Create a new thread to execute the script
    script_thread = threading.Thread(target=execute_script)
    script_thread.start()
#Running network monitoring script and display it
def network_monitoring(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\17.1_Network_Monitoring\NetworkMonitoring.py"
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
        output_text.insert(END, f"Error: {e}")
#Running behavioral analysis script and display it
def behavioral_analysis(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\BehavioralAnalytics\BehavioralAnalytics.py"
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
#Running local email account script and display it
def local_email_account(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\LocalEmailAccounts\LocalEmailAccounts.py"
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
#Running modify clipboard script and display it
def modify_clipboard(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\ModifyClipboard\ModifyClipboard.py"
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
def access_removal(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\AccountAccessRemoval\AccountAccessRemoval.py"
    try:
        # Execute the script using subprocess and catch the output
        output= subprocess.check_output(['python', script_path], universal_newlines=True)
        
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()        
#Running sysactivitymonitoring script and display it
def sys_activity_monitoring(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\SystemActivityMonitoring\SystemActivityMonitoring.py"
    try:
        # Execute the script using subprocess and catch the output
        output= subprocess.check_output(['python', script_path], universal_newlines=True)
        
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()        
#Running portscanner script and display it
def port_scanner(new_window):
    # Define a class for the new window
    class NewWindow:
        def __init__(self):
            self.output_text = Text(new_window, wrap=WORD, width=70, height=30)
            self.output_text.pack()

        # Function to update the output text
        def update_text(self, text):
            self.output_text.insert(END, text)

    # Create an instance of the NewWindow class
    new_window_instance = NewWindow()

    # Define a function to execute the port scanning script
    def run_port_scanner():
        script_path = r"C:\Users\user\Desktop\FYP\PortScanner\Portscanner.py"
        try:
            # Execute the script using subprocess and catch the output
            output = subprocess.check_output(['python', script_path], universal_newlines=True)
            
            # Update the GUI with the output
            new_window_instance.update_text(output)
            
        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during script execution
            new_window_instance.update_text(str(e))

    # Create a new thread for running the port scanner
    scanner_thread = threading.Thread(target=run_port_scanner)
    scanner_thread.start()
#Running os detection script and display it
def os_detection(new_window):
    script_path = r"C:\Users\user\Desktop\FYP\os detection\os detection.py"
    try:
        # Execute the script using subprocess and catch the output
        output= subprocess.check_output(['python', script_path], universal_newlines=True)
        
        
        # Display the output in the Text widget
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()
        output_text.insert(END, output)
        
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during script execution
        output_text = Text(new_window, wrap=WORD, width=70, height=30)
        output_text.pack()    
#Running network device discovery script and display it
def network_device_discovery(new_window):
    def execute_script():
        script_path = r"C:\Users\user\Desktop\FYP\Network Device Discovery\Network Device Discovery.py"
        try:
            # Execute the script using subprocess and catch the output
            output = subprocess.check_output(['python', script_path], universal_newlines=True)

            # Display the output in the Text widget
            new_window.output_text = Text(new_window, wrap=WORD, width=70, height=30)
            new_window.output_text.pack()
            new_window.output_text.insert(END, output)

        except subprocess.CalledProcessError as e:
            # Handle any errors that occur during script execution
            new_window.output_text = Text(new_window, wrap=WORD, width=70, height=30)
            new_window.output_text.pack()
            new_window.output_text.insert(END, f"An error occurred: {e}")

    # Create a thread to execute the script
    thread = Thread(target=execute_script)
    thread.start()   






#Open a new window when i click button for network sniffing
def open_new_window1():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Network Sniffing",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: sniffing_script(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for file and directory discovery 
def open_new_window2():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="File & Directoey Discovery",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: discovery_script(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for remote services
def open_new_window3():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Remotes Services",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda:remote_services_script(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for encrypted channel
def open_new_window4():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Encrypted Channel",font=title_font)
    label.pack()
    #Create a button in the new widow
    #for encrypted channelserver
    button_in_new_window = tk.Button(new_window, text="Encrypted Channel Server",command=lambda:encrypted_channel_server(new_window))
    button_in_new_window.pack()
    #for encrypted channelclient
    button_in_new_window = tk.Button(new_window, text="Encrypted Channel Client",command=lambda:encrypted_channel_client(new_window))
    button_in_new_window.pack()
#open a new window when i click button for Protocol tunneling
def open_new_window5():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Protocol Tunneling",font=title_font)
    label.pack()
    #Create a button in the new widow
    #for protocol tunneling server
    button_in_new_window = tk.Button(new_window, text="Protocol Tunneling Server",command=lambda:protocol_tunneling_server(new_window))
    button_in_new_window.pack()
    #for protocol tunneling client
    button_in_new_window = tk.Button(new_window, text="Protocol Tunneling Client",command=lambda:protocol_tunneling_client(new_window))
    button_in_new_window.pack()
#open a new window when i click button for DNS exfiltration
def open_new_window6():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="DNS exfiltration",font=title_font)
    label.pack()
    #Create a button in the new widow
    #for protocol tunneling server
    button_in_new_window = tk.Button(new_window, text="DNS Exfiltration Server",command=lambda:DNS_exfiltration_server(new_window))
    button_in_new_window.pack()
    #for protocol tunneling client
    button_in_new_window = tk.Button(new_window, text="DNS Exfiltration Client",command=lambda:DNS_exfiltration_client(new_window))
    button_in_new_window.pack()
#open a new window when i click button for non app layer protocol
def open_new_window7():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Non app layer protocol",font=title_font)
    label.pack()
    #Create a button in the new widow
    #for protocol tunneling server
    button_in_new_window = tk.Button(new_window, text="Non app layer protocol Server",command=lambda:non_app_layer_protocol_server(new_window))
    button_in_new_window.pack()
    #for protocol tunneling client
    button_in_new_window = tk.Button(new_window, text="Non app layer protocol Client",command=lambda:non_app_layer_protocol_client(new_window))
    button_in_new_window.pack()
    #Open a new window when i click button for network sniffing
#Open a new window when i click button for data encryption/decryption    
def open_new_window8():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Encryption/Decryption",font=title_font)
    label.pack()
    #Create a button in the new widow
    #for protocol tunneling server
    button_in_new_window = tk.Button(new_window, text="Encrypt Data",command=lambda:encrypt_data(new_window))
    button_in_new_window.pack()
    #for protocol tunneling client
    button_in_new_window = tk.Button(new_window, text="Decrypt Data",command=lambda:decrypt_data(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for decoy content    
def open_new_window9():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Decoy content",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: decoy_content(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for Burn in    
def open_new_window10():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Burn in",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: burn_in(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for Network Monitoring  
def open_new_window11():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Network Monitoring",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: network_monitoring(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for Behavioral Analysis 
def open_new_window12():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Behavioral Analysis",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: behavioral_analysis(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for local email account
def open_new_window13():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="local email account",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: local_email_account(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for modify clipboard
def open_new_window14():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Modify clipboard",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: modify_clipboard(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for user discovery
def open_new_window15():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="User Discovery",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: user_discovery(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for Account Access Removal
def open_new_window16():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Account Access Removal",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: access_removal(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for Sys Activity Monitpring
def open_new_window17():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Sys Activity Monitoring",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: sys_activity_monitoring(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for port scanning
def open_new_window18():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Port Scanner",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: port_scanner(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for os detection   
def open_new_window19():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="OS Detection",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: os_detection(new_window))
    button_in_new_window.pack()
#Open a new window when i click button for network device discovery   
def open_new_window20():
    new_window = tk.Toplevel(root)
    new_window.title("ULFG3")
    new_window.geometry("400x300")
    new_window.iconbitmap(r"C:\Users\user\Desktop\FYP\logo.ico")
    label = tk.Label(new_window, text="Network Device Discovery",font=title_font)
    label.pack()
    #Create a button in the new widow
    button_in_new_window = tk.Button(new_window, text="Start now",command=lambda: network_device_discovery(new_window))
    button_in_new_window.pack()







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
remot_services=Button(root,text="Behavioral Analisis",command=open_new_window12,padx=40,pady=30).grid(row=9,column=5,padx=50,pady=50)
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



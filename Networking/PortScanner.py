import socket
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# Function to scan a specific port
def scan_port(ip, port, text_area):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            text_area.insert(tk.END, f"Port {port}: Open\n")
        sock.close()
    except Exception as e:
        text_area.insert(tk.END, f"Error scanning port {port}: {e}\n")

# Function to start the scan
def start_scan():
    ip = ip_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())

    text_area.delete(1.0, tk.END)  # Clear previous results
    text_area.insert(tk.END, f"Starting scan on host: {ip}\n")
    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        scan_port(ip, port, text_area)

    end_time = datetime.now()
    total_time = end_time - start_time
    text_area.insert(tk.END, f"Scanning completed in: {total_time}\n")

# Create the main window
root = tk.Tk()
root.title("Port Scanner Tool")

# IP Label and Entry
ip_label = tk.Label(root, text="Target IP Address:")
ip_label.grid(row=0, column=0, padx=10, pady=10)
ip_entry = tk.Entry(root, width=30)
ip_entry.grid(row=0, column=1, padx=10, pady=10)

# Start Port Label and Entry
start_port_label = tk.Label(root, text="Start Port:")
start_port_label.grid(row=1, column=0, padx=10, pady=10)
start_port_entry = tk.Entry(root, width=10)
start_port_entry.grid(row=1, column=1, padx=10, pady=10)

# End Port Label and Entry
end_port_label = tk.Label(root, text="End Port:")
end_port_label.grid(row=2, column=0, padx=10, pady=10)
end_port_entry = tk.Entry(root, width=10)
end_port_entry.grid(row=2, column=1, padx=10, pady=10)

# Button to start scanning
scan_button = tk.Button(root, text="Start Scan", command=start_scan)
scan_button.grid(row=3, column=1, padx=10, pady=10)

# Text area to display results
text_area = scrolledtext.ScrolledText(root, width=50, height=15)
text_area.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()

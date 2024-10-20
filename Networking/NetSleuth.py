import whois
import socket
import requests
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk

def is_ip(address):
    """Check if the input is an IP address."""
    try:
        socket.inet_aton(address)
        return True
    except socket.error:
        return False

def get_ip_info(ip_address):
    """Retrieve information about an IP address using the ipinfo API."""
    try:
        response = requests.get(f"http://ipinfo.io/{ip_address}/json")
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_domain_info(domain):
    """Retrieve domain information using whois."""
    try:
        return whois.whois(domain)
    except Exception as e:
        return {"error": str(e)}

def display_info(address, ip_info=None, domain_info=None):
    """Format and display the retrieved information in the result box."""
    result_box.delete(1.0, tk.END)
    
    if is_ip(address):
        result_box.insert(tk.END, f"\n[IP Information]\n")
        result_box.insert(tk.END, "="*40 + "\n")
        if ip_info:
            result_box.insert(tk.END, f"IP Address:     {ip_info.get('ip', 'N/A')}\n")
            result_box.insert(tk.END, f"City:           {ip_info.get('city', 'N/A')}\n")
            result_box.insert(tk.END, f"Region:         {ip_info.get('region', 'N/A')}\n")
            result_box.insert(tk.END, f"Country:        {ip_info.get('country', 'N/A')}\n")
            result_box.insert(tk.END, f"Org:            {ip_info.get('org', 'N/A')}\n")
            result_box.insert(tk.END, f"Location:       {ip_info.get('loc', 'N/A')}\n")
        else:
            result_box.insert(tk.END, "Error fetching IP information.\n")
    else:
        result_box.insert(tk.END, f"\n[Domain Information]\n")
        result_box.insert(tk.END, "="*40 + "\n")
        if domain_info:
            result_box.insert(tk.END, f"Domain Name:    {domain_info.domain_name}\n")
            result_box.insert(tk.END, f"Registrar:      {domain_info.registrar}\n")
            result_box.insert(tk.END, f"Creation Date:  {domain_info.creation_date}\n")
            result_box.insert(tk.END, f"Expiration Date:{domain_info.expiration_date}\n")
            result_box.insert(tk.END, f"Name Servers:   {', '.join(domain_info.name_servers)}\n")
            result_box.insert(tk.END, f"Emails:         {domain_info.emails}\n")
            result_box.insert(tk.END, f"DNSSEC:         {domain_info.dnssec}\n")
            result_box.insert(tk.END, f"Country:        {domain_info.country}\n")
        else:
            result_box.insert(tk.END, "Error fetching domain information.\n")

    # Add a footer
    result_box.insert(tk.END, "\n" + "="*40 + "\n")

def retrieve_info():
    """Determine if input is IP or domain and fetch respective info."""
    address = entry.get()
    if not address:
        messagebox.showerror("Input Error", "Please enter an IP address or domain name!")
        return
    
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, f"Fetching information for {address}...\n\n")

    # Run the info retrieval in a separate thread to keep UI responsive
    threading.Thread(target=fetch_and_display_info, args=(address,)).start()

def fetch_and_display_info(address):
    """Fetch both IP/Domain info and display."""
    ip_info = None
    domain_info = None

    if is_ip(address):
        ip_info = get_ip_info(address)
    else:
        domain_info = get_domain_info(address)
    
    # After fetching, display the information in the result box
    display_info(address, ip_info, domain_info)

def clear_text():
    """Clear input and output fields."""
    entry.delete(0, tk.END)
    result_box.delete(1.0, tk.END)

# Set up the GUI window
root = tk.Tk()
root.title("NetSleuth - IP & Domain Info")
root.geometry("700x650")  # Increased size for better readability

# Add some styling to improve the appearance
root.configure(bg="#2c3e50")

# Configure root window grid layout to make it responsive
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)

# Title label
label_title = tk.Label(root, text="NetSleuth", font=("Arial", 20, "bold"), bg="#2c3e50", fg="#ecf0f1")
label_title.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

# Subtitle
label_subtitle = tk.Label(root, text="IP & Domain Information Tool", font=("Arial", 14), bg="#2c3e50", fg="#bdc3c7")
label_subtitle.grid(row=1, column=0, pady=5, padx=10, sticky="nsew")

# Input frame
frame_input = tk.Frame(root, bg="#34495e")
frame_input.grid(row=2, column=0, pady=10, padx=10, sticky="ew")
frame_input.grid_columnconfigure(1, weight=1)

label = tk.Label(frame_input, text="Enter IP/Domain:", font=("Arial", 12), bg="#34495e", fg="#ecf0f1")
label.grid(row=0, column=0, padx=10, sticky="w")

entry = tk.Entry(frame_input, font=("Arial", 12), width=50)
entry.grid(row=0, column=1, pady=5, padx=10, sticky="ew")

# Buttons frame
frame_buttons = tk.Frame(root, bg="#2c3e50")
frame_buttons.grid(row=3, column=0, pady=10, padx=10, sticky="ew")
frame_buttons.grid_columnconfigure(0, weight=1)
frame_buttons.grid_columnconfigure(1, weight=1)

button_get_info = tk.Button(frame_buttons, text="Get Info", command=retrieve_info, bg="#27ae60", fg="white", font=("Arial", 12))
button_get_info.grid(row=0, column=0, pady=5, padx=5, sticky="ew")

button_clear = tk.Button(frame_buttons, text="Clear", command=clear_text, bg="#c0392b", fg="white", font=("Arial", 12))
button_clear.grid(row=0, column=1, pady=5, padx=5, sticky="ew")

# Result box for displaying output
result_box = scrolledtext.ScrolledText(root, width=70, height=25, font=("Courier", 10), bg="#ecf0f1", fg="#2c3e50", wrap=tk.WORD)
result_box.grid(row=4, column=0, pady=10, padx=10, sticky="nsew")

# Start the GUI main loop
root.mainloop()
import whois
import tkinter as tk
from tkinter import messagebox, scrolledtext

def get_domain_info():
    domain = entry.get()
    if not domain:
        messagebox.showerror("Input Error", "Please enter a domain name!")
        return
    
    try:
        # Get the domain information using whois
        domain_info = whois.whois(domain)
        # Clear the result box before showing new information
        result_box.delete(1.0, tk.END)
        
        # Format and display the domain information
        formatted_info = f"""
        =============================
        Domain Name:        {domain_info.domain_name}
        =============================

        📍 Registrar:       {domain_info.registrar}
        📅 Creation Date:   {domain_info.creation_date}
        📅 Expiration Date: {domain_info.expiration_date}
        🛠️  Last Updated:   {domain_info.updated_date}

        =============================
        🔍 Status:          {domain_info.status}
        =============================

        🌐 Name Servers:
        - {', '.join(domain_info.name_servers)}

        📧 Contact Email(s):
        - {domain_info.emails}

        🔐 DNSSEC:          {domain_info.dnssec}
        🌍 Country:         {domain_info.country}
        =============================
        """
        result_box.insert(tk.END, formatted_info)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve information: {str(e)}")

def clear_text():
    entry.delete(0, tk.END)
    result_box.delete(1.0, tk.END)

# Set up the GUI window
root = tk.Tk()
root.title("Domain Information Tool")
root.geometry("600x500")  # Set initial size

# Configure root window grid layout to make it responsive
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)

# Title label
label_title = tk.Label(root, text="Domain Information Tool", font=("Arial", 16))
label_title.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

# Input label and text field
frame_input = tk.Frame(root)
frame_input.grid(row=1, column=0, pady=5, padx=10, sticky="nsew")
frame_input.grid_columnconfigure(1, weight=1)

label = tk.Label(frame_input, text="Enter Domain Name:", font=("Arial", 12))
label.grid(row=0, column=0, padx=10, sticky="w")

entry = tk.Entry(frame_input, width=50)
entry.grid(row=0, column=1, pady=5, padx=10, sticky="ew")

# Buttons
frame_buttons = tk.Frame(root)
frame_buttons.grid(row=3, column=0, pady=5, padx=10, sticky="nsew")
frame_buttons.grid_columnconfigure(0, weight=1)
frame_buttons.grid_columnconfigure(1, weight=1)

button_get_info = tk.Button(frame_buttons, text="Get Domain Info", command=get_domain_info, bg="#4CAF50", fg="white")
button_get_info.grid(row=0, column=0, pady=5, padx=5, sticky="ew")

button_clear = tk.Button(frame_buttons, text="Clear", command=clear_text, bg="#f44336", fg="white")
button_clear.grid(row=0, column=1, pady=5, padx=5, sticky="ew")

# ScrolledText box for showing the result with increased size
result_box = scrolledtext.ScrolledText(root, width=70, height=18, font=("Courier", 10))
result_box.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")

# Start the GUI main loop
root.mainloop()

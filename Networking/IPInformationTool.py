import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import requests

# Function to get IP information
def get_ip_info():
    ip_address = ip_entry.get().strip()
    if not ip_address:
        messagebox.showwarning("Input Error", "Please enter a valid IP address.")
        return

    try:
        # Fetch IP information using the ipinfo.io API
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()
        
        # Display the result
        text_area.delete(1.0, tk.END)  # Clear previous results
        text_area.insert(tk.END, f"IP Information for {ip_address}:\n\n")
        
        for key, value in data.items():
            text_area.insert(tk.END, f"{key.capitalize()}: {value}\n")
    except Exception as e:
        text_area.insert(tk.END, f"Error retrieving data: {e}\n")

# Function to clear the text area and input field
def clear_text():
    ip_entry.delete(0, tk.END)
    text_area.delete(1.0, tk.END)

# Create the main window
root = tk.Tk()
root.title("IP Information Tool")
root.geometry("500x400")
root.config(bg="#f0f4f7")  # Light grayish blue background

# Set font styles
title_font = ("Arial", 16, "bold")
label_font = ("Arial", 12)
button_font = ("Arial", 10, "bold")

# Title label
title_label = tk.Label(root, text="IP Information Tool", font=title_font, bg="#f0f4f7", fg="#2c3e50")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# IP Address Label and Entry
ip_label = tk.Label(root, text="Enter IP Address:", font=label_font, bg="#f0f4f7", fg="#34495e")
ip_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

ip_entry = tk.Entry(root, width=30, font=label_font, bd=2, relief="groove")
ip_entry.grid(row=1, column=1, padx=10, pady=10)

# Button to fetch IP info
get_info_button = tk.Button(root, text="Get IP Info", font=button_font, bg="#3498db", fg="white", width=12, 
                            relief="raised", command=get_ip_info)
get_info_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

# Button to clear the text area
clear_button = tk.Button(root, text="Clear", font=button_font, bg="#e74c3c", fg="white", width=12, 
                         relief="raised", command=clear_text)
clear_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

# Text area to display results
text_area = scrolledtext.ScrolledText(root, width=58, height=12, font=("Arial", 10), wrap=tk.WORD, bd=2, relief="groove")
text_area.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()

import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import tkinter as tk
from tkinter import messagebox

# Function to get phone number information
def get_phone_info():
    phone_number = entry.get()
    try:
        # Parsing the phone number
        parsed_number = phonenumbers.parse(phone_number)

        # Getting country and location information
        country = geocoder.description_for_number(parsed_number, "en")
        
        # Getting carrier information
        service_provider = carrier.name_for_number(parsed_number, "en")
        
        # Getting timezone information
        time_zones = timezone.time_zones_for_number(parsed_number)

        # Displaying information in a message box
        info = (
            f"Phone Number: {phone_number}\n"
            f"Country/Location: {country}\n"
            f"Service Provider: {service_provider}\n"
            f"Timezone(s): {', '.join(time_zones)}"
        )
        messagebox.showinfo("Phone Number Information", info)
    except phonenumbers.NumberParseException:
        messagebox.showerror("Error", "Invalid phone number format!")

# Setting up the GUI
app = tk.Tk()
app.title("Phone Number Information Tool")
app.geometry("400x200")

# Label and Entry for Phone Number
label = tk.Label(app, text="Enter phone number (with country code):")
label.pack(pady=10)

entry = tk.Entry(app, width=30)
entry.pack(pady=5)

# Button to Get Information
button = tk.Button(app, text="Get Information", command=get_phone_info)
button.pack(pady=20)

app.mainloop()

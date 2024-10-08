import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Basic Tkinter Program")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

# Define a function to change the label text
def change_text():
    label.config(text="Button Clicked!")

# Create a button widget
button = tk.Button(root, text="Click Me", command=change_text)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

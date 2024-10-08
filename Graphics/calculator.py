import tkinter as tk

# Function to update the expression in the display
def update_display(value):
    current_text = display_var.get()
    display_var.set(current_text + value)

# Function to evaluate the expression and display the result
def evaluate_expression():
    try:
        result = str(eval(display_var.get()))
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Function to clear the display
def clear_display():
    display_var.set("")

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Create a StringVar to hold the display text
display_var = tk.StringVar()

# Create a display entry widget
display_entry = tk.Entry(root, textvariable=display_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
display_entry.grid(row=0, column=0, columnspan=4)

# Create buttons for the calculator
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for text in button_texts:
    if text == "=":
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=evaluate_expression)
    elif text == "C":
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=clear_display)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: update_display(t))
    
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the Tkinter event loop
root.mainloop()

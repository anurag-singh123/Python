import tkinter as tk
from tkinter import messagebox, filedialog
import json
from datetime import datetime

class FinanceManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Manager")

        self.transactions = []

        # Create UI elements
        self.create_widgets()
        self.create_summary_section()

    def create_widgets(self):
        # Entry fields for transaction details
        self.date_label = tk.Label(self.root, text="Date (YYYY-MM-DD)", font=('Arial', 12))
        self.date_label.pack()
        self.date_entry = tk.Entry(self.root, font=('Arial', 12))
        self.date_entry.pack(pady=5)

        self.desc_label = tk.Label(self.root, text="Description", font=('Arial', 12))
        self.desc_label.pack()
        self.desc_entry = tk.Entry(self.root, font=('Arial', 12))
        self.desc_entry.pack(pady=5)

        self.amount_label = tk.Label(self.root, text="Amount", font=('Arial', 12))
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.root, font=('Arial', 12))
        self.amount_entry.pack(pady=5)

        self.category_label = tk.Label(self.root, text="Category (Income/Expense)", font=('Arial', 12))
        self.category_label.pack()
        self.category_entry = tk.Entry(self.root, font=('Arial', 12))
        self.category_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Transaction", command=self.add_transaction, font=('Arial', 12))
        self.add_button.pack(pady=10)

        self.transaction_listbox = tk.Listbox(self.root, width=80, height=10, font=('Arial', 12))
        self.transaction_listbox.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Save Transactions", command=self.save_transactions, font=('Arial', 12))
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(self.root, text="Load Transactions", command=self.load_transactions, font=('Arial', 12))
        self.load_button.pack(pady=5)

    def create_summary_section(self):
        self.summary_frame = tk.Frame(self.root)
        self.summary_frame.pack(pady=10)

        self.total_income_label = tk.Label(self.summary_frame, text="Total Income: $0.00", font=('Arial', 12))
        self.total_income_label.grid(row=0, column=0, padx=10)

        self.total_expense_label = tk.Label(self.summary_frame, text="Total Expenses: $0.00", font=('Arial', 12))
        self.total_expense_label.grid(row=0, column=1, padx=10)

        self.balance_label = tk.Label(self.summary_frame, text="Balance: $0.00", font=('Arial', 12))
        self.balance_label.grid(row=0, column=2, padx=10)

    def add_transaction(self):
        date = self.date_entry.get()
        desc = self.desc_entry.get()
        amount = self.amount_entry.get()
        category = self.category_entry.get()

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Invalid Amount", "Please enter a valid number for the amount.")
            return

        if category.lower() not in ["income", "expense"]:
            messagebox.showerror("Invalid Category", "Category must be 'Income' or 'Expense'.")
            return

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
            return

        transaction = {"date": date, "desc": desc, "amount": amount, "category": category}
        self.transactions.append(transaction)
        self.update_listbox()
        self.update_summary()

        self.date_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

    def update_listbox(self):
        self.transaction_listbox.delete(0, tk.END)
        for transaction in self.transactions:
            display_text = f"{transaction['date']} - {transaction['desc']} - ${transaction['amount']:,.2f} - {transaction['category']}"
            self.transaction_listbox.insert(tk.END, display_text)

    def update_summary(self):
        total_income = sum(t['amount'] for t in self.transactions if t['category'].lower() == 'income')
        total_expense = sum(t['amount'] for t in self.transactions if t['category'].lower() == 'expense')
        balance = total_income - total_expense

        self.total_income_label.config(text=f"Total Income: ${total_income:,.2f}")
        self.total_expense_label.config(text=f"Total Expenses: ${total_expense:,.2f}")
        self.balance_label.config(text=f"Balance: ${balance:,.2f}")

    def save_transactions(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(self.transactions, file)
            messagebox.showinfo("Info", "Transactions saved successfully!")

    def load_transactions(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                self.transactions = json.load(file)
            self.update_listbox()
            self.update_summary()
            messagebox.showinfo("Info", "Transactions loaded successfully!")

# Create the main application window
root = tk.Tk()
app = FinanceManagerApp(root)

# Run the Tkinter event loop
root.mainloop()

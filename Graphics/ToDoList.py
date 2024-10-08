import tkinter as tk
from tkinter import messagebox, filedialog
import json

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []
        
        # Create UI elements
        self.task_entry = tk.Entry(root, width=50, font=('Arial', 14))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=('Arial', 12))
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=15, font=('Arial', 14))
        self.task_listbox.pack(pady=10)

        self.complete_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed, font=('Arial', 12))
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, font=('Arial', 12))
        self.delete_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks, font=('Arial', 12))
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks, font=('Arial', 12))
        self.load_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["completed"] = True
            self.update_listbox()

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_listbox()

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as file:
                json.dump(self.tasks, file)
            messagebox.showinfo("Info", "Tasks saved successfully!")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as file:
                self.tasks = json.load(file)
            self.update_listbox()
            messagebox.showinfo("Info", "Tasks loaded successfully!")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = task["task"]
            if task["completed"]:
                display_text += " (Completed)"
            self.task_listbox.insert(tk.END, display_text)

# Create the main application window
root = tk.Tk()
app = TodoApp(root)

# Run the Tkinter event loop
root.mainloop()

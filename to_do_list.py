import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []
        
        # Task input field
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        
        # Add task button
        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack()
        
        # Task list
        self.task_list = tk.Listbox(root, width=50)
        self.task_list.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Buttons for marking tasks as complete and deleting tasks
        self.complete_button = tk.Button(root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.RIGHT, padx=5)
        
        # Load tasks
        self.load_tasks()
    
    def load_tasks(self):
        for task in self.tasks:
            self.task_list.insert(tk.END, task)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
    
    def mark_complete(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            self.task_list.itemconfig(selected_task_index, {'bg': 'light grey', 'fg': 'grey'})
        except IndexError:
            messagebox.showwarning("No Task Selected", "Please select a task to mark as complete.")
    
    def delete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

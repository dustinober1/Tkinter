import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker App")
        
        self.expenses = {}
        
        # Expense input fields
        tk.Label(root, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(root, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Button to add expense
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=2, columnspan=2, padx=5, pady=5)
        
        # Button to view spending trends
        self.view_trends_button = tk.Button(root, text="View Spending Trends", command=self.view_spending_trends)
        self.view_trends_button.grid(row=3, columnspan=2, padx=5, pady=5)
    
    def add_expense(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        
        if amount and category:
            try:
                amount = float(amount)
                if category in self.expenses:
                    self.expenses[category] += amount
                else:
                    self.expenses[category] = amount
                messagebox.showinfo("Expense Added", "Expense added successfully.")
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid amount.")
        else:
            messagebox.showwarning("Incomplete Input", "Please enter both amount and category.")
        
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
    
    def view_spending_trends(self):
        if not self.expenses:
            messagebox.showwarning("No Data", "No expense data available.")
            return
        
        # Plotting spending trends
        fig, ax = plt.subplots()
        ax.bar(self.expenses.keys(), self.expenses.values())
        ax.set_xlabel('Category')
        ax.set_ylabel('Amount')
        ax.set_title('Spending Trends')
        
        # Embedding the plot in Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

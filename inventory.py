import tkinter as tk

class InventoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        
        # Entry fields for product details
        tk.Label(root, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
        self.product_name_entry = tk.Entry(root)
        self.product_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(root, text="Stock Level:").grid(row=1, column=0, padx=5, pady=5)
        self.stock_level_entry = tk.Entry(root)
        self.stock_level_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Button to add product
        self.add_button = tk.Button(root, text="Add Product", command=self.add_product)
        self.add_button.grid(row=2, columnspan=2, padx=5, pady=5)
        
        # Display area for product list
        self.product_list = tk.Listbox(root, width=50)
        self.product_list.grid(row=3, columnspan=2, padx=5, pady=5)
    
    def add_product(self):
        product_name = self.product_name_entry.get()
        stock_level = self.stock_level_entry.get()
        
        if product_name and stock_level:
            self.product_list.insert(tk.END, f"{product_name} - Stock: {stock_level}")
            self.product_name_entry.delete(0, tk.END)
            self.stock_level_entry.delete(0, tk.END)
        else:
            tk.messagebox.showwarning("Incomplete Input", "Please enter both product name and stock level.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagementApp(root)
    root.mainloop()

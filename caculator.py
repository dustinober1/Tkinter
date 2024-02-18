import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.expression = ""
        
        # Entry field to display expression
        self.display = tk.Entry(root, width=20, font=('Arial', 14), bd=5, justify=tk.RIGHT)
        self.display.grid(row=0, column=0, columnspan=4)
        
        # Buttons for digits and operations
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        for (text, row, column) in buttons:
            button = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)
    
    def on_button_click(self, text):
        if text == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif text == 'C':
            self.expression = ""
        else:
            self.expression += text
        
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

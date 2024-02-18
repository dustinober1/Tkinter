import tkinter as tk  
from tkinter import ttk, messagebox  
  
root = tk.Tk()  
root.title("Test App")  
root.resizable(True, False)  
  
widget = tk.Button(root, text = "Button")  
widget.pack()  
  
root.mainloop() 
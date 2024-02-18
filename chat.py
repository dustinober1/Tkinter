import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")
        
        # ScrolledText for displaying messages
        self.chat_display = ScrolledText(root, width=50, height=20, wrap=tk.WORD)
        self.chat_display.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Entry field for typing messages
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Button to send message
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=5)
    
    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.chat_display.insert(tk.END, "You: " + message + "\n")
            self.message_entry.delete(0, tk.END)
        else:
            tk.messagebox.showwarning("Empty Message", "Please enter a message.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()

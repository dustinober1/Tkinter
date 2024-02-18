import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

class NoteTakingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note-taking App")
        
        # ScrolledText for displaying and editing notes
        self.note_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.note_text.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Button to save note
        self.save_button = tk.Button(root, text="Save Note", command=self.save_note)
        self.save_button.pack(pady=5)
    
    def save_note(self):
        note = self.note_text.get("1.0", tk.END)
        # You can implement saving the note to a file or database here
        tk.messagebox.showinfo("Note Saved", "Note saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteTakingApp(root)
    root.mainloop()

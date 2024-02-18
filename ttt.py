import tkinter as tk
from tkinter import messagebox

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.current_player = "X"
        self.board = [['' for _ in range(3)] for _ in range(3)]
        
        # Buttons for the game board
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(root, text='', width=10, height=4,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        
    def on_button_click(self, i, j):
        if self.board[i][j] == '':
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                tk.messagebox.showinfo("Winner", f"{self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                tk.messagebox.showinfo("Draw", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True
    
    def reset_board(self):
        self.current_player = "X"
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()

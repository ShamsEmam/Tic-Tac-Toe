import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe: Player vs AI")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        self.window.mainloop()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=('Helvetica', 20), height=3, width=6,
                                   command=lambda row=i, col=j: self.player_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def player_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", state="disabled")
            if self.check_winner(self.board, "X"):
                messagebox.showinfo("Game Over", "You win!")
                self.reset_board()
            elif self.is_draw(self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.ai_move()

    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            i, j = best_move
            self.board[i][j] = "O"
            self.buttons[i][j].config(text="O", state="disabled")
            if self.check_winner(self.board, "O"):
                messagebox.showinfo("Game Over", "AI wins!")
                self.reset_board()
            elif self.is_draw(self.board):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(board, "O"):
            return 1
        elif self.check_winner(board, "X"):
            return -1
        elif self.is_draw(board):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "X"
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ""
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, board, player):
        # Check rows and columns
        for i in range(3):
            if all([cell == player for cell in board[i]]):
                return True
            if all([board[j][i] == player for j in range(3)]):
                return True
        # Check diagonals
        if all([board[i][i] == player for i in range(3)]):
            return True
        if all([board[i][2 - i] == player for i in range(3)]):
            return True
        return False

    def is_draw(self, board):
        return all([cell != "" for row in board for cell in row])

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="", state="normal")

if __name__ == "__main__":
    TicTacToe()
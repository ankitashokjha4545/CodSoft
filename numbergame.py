#NUMBER GUESSING GAME TASK - 1 FROM [CODXO]
import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.setup_gui()

    def setup_gui(self):
        # Label and entry for user input
        tk.Label(self.root, text="Enter your guess (1-100):").pack(pady=10)
        self.guess_entry = tk.Entry(self.root, width=20)
        self.guess_entry.pack()

        # Button to submit guess
        submit_btn = tk.Button(self.root, text="Guess", command=self.check_guess)
        submit_btn.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                messagebox.showinfo("Result", "Too low! Try again.")
            elif guess > self.secret_number:
                messagebox.showinfo("Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"Correct! You guessed the number {self.secret_number} in {self.attempts} attempts.")
                self.reset_game()

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def reset_game(self):
        # Generate new secret number and reset attempts
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        messagebox.showinfo("New Game", "Let's play again! I've picked a new number between 1 and 100.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    game.run()

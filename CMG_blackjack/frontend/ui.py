import tkinter as tk
from logic.blackjack_logic import BlackjackGame
from backend.score import ScoreManager

class BlackjackUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Game")
        # Add UI components and logic here

def main():
    root = tk.Tk()
    app = BlackjackUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


import tkinter as tk
from logic.blackjack_logic import BlackjackGame
from backend.score import ScoreManager

class BlackjackUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Game")
        # Add UI components and logic here
        
        # Initialize game logic and score manager
        self.game = BlackjackGame()
        self.score_manager = ScoreManager()

        # UI components
        self.label = tk.Label(root, text="Welcome to Blackjack!")
        self.label.pack()

        self.play_button = tk.Button(root, text="Play", command=self.start_game)
        self.play_button.pack()

        self.hit_button = tk.Button(root, text="Hit", command=self.player_hit, state=tk.DISABLED)
        self.hit_button.pack()

        self.stand_button = tk.Button(root, text="Stand", command=self.player_stand, state=tk.DISABLED)
        self.stand_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

    def start_game(self):
        self.play_button.config(state=tk.DISABLED)
        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)
    def start_game(self):
        self.play_button.config(state=tk.DISABLED)
        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)

        self.game.deal_initial_cards()
        self.label.config(text="Your Hand: " + ", ".join(self.game.player_hand))
        
    def player_hit(self):
        self.game.player_hit()
        self.label.config(text="Your Hand: " + ", ".join(self.game.player_hand))

        if self.game.player_bust:
            self.end_game()
        
    def player_stand(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.game.dealer_turn()
        self.end_game()
        
    def end_game(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        
        result = self.game.determine_winner()
        self.label.config(text=result)
        
        if result.startswith("You"):
            self.score_manager.add_score("Player", 1)
        elif result.startswith("Dealer"):
            self.score_manager.add_score("Dealer", 1)

    def show_scores(self):
        scores = self.score_manager.get_scores()
        score_text = "\n".join(f"{name}: {score}" for name, score in scores)
        messagebox.showinfo("Scores", score_text)

def main():
    root = tk.Tk()
    app = BlackjackUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


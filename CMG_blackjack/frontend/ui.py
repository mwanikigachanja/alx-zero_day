import tkinter as tk
from tkinter import messagebox
import pygame
from PIL import Image, ImageTk
# Import the PIL library for image handling
from logic.game_logic import BlackjackGame
from backend.score import ScoreManager

class BlackjackUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CMG MASTER BLACKJACK")
        self.player_chips = 100
        bet_amount = int(self.bet_entry.get())
        self.game.place_bet(bet_amount)
        # Add UI components and logic here
        
        # Initialize game logic and score manager
        self.game = BlackjackGame()
        self.score_manager = ScoreManager()
        self.animation_frames = []  # List to store animation frames
        self.current_frame = 0
        # Initialize pygame mixer for sound effects
        pygame.mixer.init()

        # UI components
        self.label = tk.Label(root, text="Welcome to Blackjack!")
        self.label.pack()

        self.chips_label = tk.Label(root, text="Chips: 100")
        self.chips_label.pack()

        self.play_button = tk.Button(root, text="Play", command=self.start_game)
        self.play_button.pack()

        self.hit_button = tk.Button(root, text="Hit", command=self.player_hit, state=tk.DISABLED)
        self.hit_button.pack()

        self.stand_button = tk.Button(root, text="Stand", command=self.player_stand, state=tk.DISABLED)
        self.stand_button.pack()

        self.double_button = tk.Button(root, text="Double Down", command=self.double_down, state=tk.DISABLED)
        self.double_button.pack()

        self.split_button = tk.Button(root, text="Split", command=self.split, state=tk.DISABLED)
        self.split_button.pack()

        self.insurance_button = tk.Button(root, text="Insurance", command=self.take_insurance, state=tk.DISABLED)
        self.insurance_button.pack()

        self.animate_button = tk.Button(root, text="Animate", command=self.animate_dealing)
        self.animate_button.pack()

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()

    def animate_dealing(self):
        self.animate_button.config(state=tk.DISABLED)
        self.current_frame = 0
        self.animate_frame()

    def animate_frame(self):
        if self.current_frame < len(self.animation_frames):
            self.label.config(text=self.animation_frames[self.current_frame])
            self.current_frame += 1
            self.root.after(500, self.animate_frame)  # Delay between frames
        else:
            self.animate_button.config(state=tk.NORMAL)
            self.label.config(text="Your Hand: " + ", ".join(self.game.player_hand))
            self.root.update()

    def start_game(self):
        self.play_button.config(state=tk.DISABLED)
        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)
        self.double_button.config(state=tk.NORMAL)
        self.split_button.config(state=tk.NORMAL)
        self.insurance_button.config(state=tk.NORMAL)

        self.game.deal_initial_cards()
        self.label.config(text="Your Hand: " + ", ".join(self.game.player_hand))

        # Update UI with player's initial hand
        self.update_ui()

    def player_hit(self):
        self.game.player_hit()
        self.label.config(text="Your Hand: " + ", ".join(self.game.player_hand))

        if self.game.player_bust:
            self.end_game()

    def update_ui(self):
        # Update UI components with current game state
        player_hand_text = "Your Hand: " + ", ".join(self.game.player_hand)
        self.label.config(text=player_hand_text)

    def player_stand(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.game.dealer_turn()
        self.end_game()
        
    def end_game(self):
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
        self.game.calculate_payout()
        self.update_player_chips(self.game.payout)
        self.game.reset_game_state()

        result = self.game.determine_winner()
        self.label.config(text=result)
        
        if result.startswith("You"):
            self.score_manager.add_score("Player", 1)
        elif result.startswith("Dealer"):
            self.score_manager.add_score("Dealer", 1)

        self.update_ui()

    def show_scores(self):
        scores = self.score_manager.get_scores()
        score_text = "\n".join(f"{name}: {score}" for name, score in scores)
        messagebox.showinfo("Scores", score_text)

    def double_down(self):
        if self.player_chips >= self.bet_amount * 2:
            self.bet_amount *= 2
            self.hit_button.config(state=tk.DISABLED)
            self.stand_button.config(state=tk.DISABLED)
            self.player_hit()
            self.player_stand()
            self.game.double_down()

    def split(self):
        # Logic for splitting pairs (requires more detailed game implementation)
        self.game.split()

    def take_insurance(self):
        # Logic for taking insurance against dealer's potential blackjack
        self.game.take_insurance()

    def update_chips_label(self):
        self.chips_label.config(text="Chips: " + str(self.player_chips))
        self.bet_label.config(text="Bet: " + str(self.bet_amount))

    def play_sound(self, sound_file):
        # Implement sound playing logic
        sound = pygame.mixer.Sound(sound_file)
        sound.play()

    def animate_dealing(self):
        self.play_sound("deal_sound.wav")  # Play deal sound effect
        self.play_sound("deal_sound.wav")  # Play deal sound effect
        # Implement card dealing animation using animation frames
        self.animate_button.config(state=tk.DISABLED)
        self.current_frame = 0
        self.animate_frame()

    def animate_frame(self):
        if self.current_frame < len(self.animation_frames):
            frame = self.animation_frames[self.current_frame]

            # Display image if the frame is an image path
            if isinstance(frame, str):
                image = Image.open(frame)
                image = image.resize((200, 300))  # Resize the image to fit the UI
                photo = ImageTk.PhotoImage(image=image)
                self.label.config(image=photo)
                self.label.image = photo
            else:
                self.label.config(text=frame)

            self.current_frame += 1
            self.root.after(500, self.animate_frame)  # Delay between frames
        else:
            self.animate_button.config(state=tk.NORMAL)
            self.label.config(text="Your Hand: " + ", ".join(self.game.player_hand))
            self.root.update()


def main():
    root = tk.Tk()
    app = BlackjackUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()


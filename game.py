import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        # Variables for tracking user and computer choices
        self.user_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()

        # Variables for tracking scores
        self.user_score = tk.IntVar()
        self.computer_score = tk.IntVar()

        # Create the result label as an instance variable
        self.result_label = None

        self.create_widgets()

    def create_widgets(self):
        # Style configuration for a more visually appealing design
        style = ttk.Style()
        style.configure('TFrame', background='#E6E6E6')
        style.configure('TLabel', background='#E6E6E6', font=('Arial', 36))  # Increase font size

        # Frame to hold the widgets
        main_frame = ttk.Frame(self.root, padding=(100, 50))  # Increase padding
        main_frame.grid(row=0, column=0)

        # Label for user prompt
        prompt_label = ttk.Label(main_frame, text="Rock, Paper, or Scissors:", font=('Arial', 36))  # Increase font size
        prompt_label.grid(row=0, column=0, columnspan=3, pady=(0, 40), sticky='w')

        # Images for Rock, Paper, and Scissors
        rock_img = Image.open("rock.jpg")
        rock_img = rock_img.resize((150, 150), Image.ANTIALIAS)  # Increase image size
        self.rock_photo = ImageTk.PhotoImage(rock_img)

        paper_img = Image.open("paper.jpg")
        paper_img = paper_img.resize((150, 150), Image.ANTIALIAS)
        self.paper_photo = ImageTk.PhotoImage(paper_img)

        scissors_img = Image.open("scissors.jpg")
        scissors_img = scissors_img.resize((150, 150), Image.ANTIALIAS)
        self.scissors_photo = ImageTk.PhotoImage(scissors_img)

        # Buttons with images for Rock, Paper, and Scissors
        rock_button = ttk.Button(main_frame, image=self.rock_photo, command=lambda: self.make_choice("Rock"))
        rock_button.grid(row=1, column=0, padx=20, pady=20)

        paper_button = ttk.Button(main_frame, image=self.paper_photo, command=lambda: self.make_choice("Paper"))
        paper_button.grid(row=1, column=1, padx=20, pady=20)

        scissors_button = ttk.Button(main_frame, image=self.scissors_photo, command=lambda: self.make_choice("Scissors"))
        scissors_button.grid(row=1, column=2, padx=20, pady=20)

        # Display area for game result
        self.result_label = ttk.Label(main_frame, text="", font=('Arial', 36))  # Increase font size
        self.result_label.grid(row=2, column=0, columnspan=3, pady=40)

        # Label to display scores
        scores_label = ttk.Label(main_frame, textvariable=self.get_scores_var(), font=('Arial', 36))  # Increase font size
        scores_label.grid(row=3, column=0, columnspan=3, pady=40)

    def get_scores_var(self):
        return tk.StringVar(value="Scores: User {} - {} Computer".format(self.user_score.get(), self.computer_score.get()))

    def make_choice(self, choice):
        self.user_choice.set(choice)
        self.play_game()

    def play_game(self):
        choices = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(choices)
        self.computer_choice.set(computer_choice)

        user_choice = self.user_choice.get().capitalize()

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (user_choice == 'Rock' and computer_choice == 'Scissors') or
            (user_choice == 'Paper' and computer_choice == 'Rock') or
            (user_choice == 'Scissors' and computer_choice == 'Paper')
        ):
            result = f"You win! {user_choice} beats {computer_choice}."
            self.user_score.set(self.user_score.get() + 1)
        else:
            result = f"You lose! {computer_choice} beats {user_choice}."
            self.computer_score.set(self.computer_score.get() + 1)

        # Update scores and result labels
        scores_var = self.get_scores_var()
        scores_var.set("Scores: User {} - {} Computer".format(self.user_score.get(), self.computer_score.get()))

        self.result_label.config(text=" {}".format(result))

def main():
    # Create the main window
    root = tk.Tk()
    app = RockPaperScissorsGame(root)

    # Configure the window appearance
    root.configure(bg='#E6E6E6')
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Fullscreen

    # Maximize the window
    root.state('zoomed')

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()

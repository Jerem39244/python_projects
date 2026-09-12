import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play_game(player_choice):
    """Play one round of Rock Paper Scissors."""

   
    computer_choice = random.choice(choices)

    player_label.config(text=f"You chose: {player_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        result = "It's a tie!"

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"

    else:
        result = "Computer wins!"

    result_label.config(text=result)


def reset_game():
    """Reset the game display."""

    player_label.config(text="You chose: ")
    computer_label.config(text="Computer chose: ")
    result_label.config(text="Choose Rock, Paper, or Scissors!")

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("500x400")
window.config(bg="#222222")

title_label = tk.Label(
    window,
    text="Rock Paper Scissors",
    font=("Arial", 24, "bold"),
    bg="#222222",
    fg="white"
)

title_label.pack(pady=20)

instruction_label = tk.Label(
    window,
    text="Choose your move:",
    font=("Arial", 16),
    bg="#222222",
    fg="white"
)

instruction_label.pack(pady=10)


button_frame = tk.Frame(window, bg="#222222")
button_frame.pack(pady=10)

rock_button = tk.Button(
    button_frame,
    text="Rock",
    font=("Arial", 14),
    width=10,
    command=lambda: play_game("Rock")
)

paper_button = tk.Button(
    button_frame,
    text="Paper",
    font=("Arial", 14),
    width=10,
    command=lambda: play_game("Paper")
)

scissors_button = tk.Button(
    button_frame,
    text="Scissors",
    font=("Arial", 14),
    width=10,
    command=lambda: play_game("Scissors")
)

rock_button.grid(row=0, column=0, padx=5)
paper_button.grid(row=0, column=1, padx=5)
scissors_button.grid(row=0, column=2, padx=5)

player_label = tk.Label(
    window,
    text="You chose: ",
    font=("Arial", 14),
    bg="#222222",
    fg="white"
)

player_label.pack(pady=10)


computer_label = tk.Label(
    window,
    text="Computer chose: ",
    font=("Arial", 14),
    bg="#222222",
    fg="white"
)

computer_label.pack(pady=10)


result_label = tk.Label(
    window,
    text="Choose Rock, Paper, or Scissors!",
    font=("Arial", 18, "bold"),
    bg="#222222",
    fg="#00ff99"
)

result_label.pack(pady=20)

reset_button = tk.Button(
    window,
    text="Reset",
    font=("Arial", 12),
    width=10,
    command=reset_game
)

reset_button.pack(pady=10)

window.mainloop()

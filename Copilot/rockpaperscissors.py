"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""

import random
import tkinter as tk
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_player_choice():
    while True:
        player_input = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        # Map shortcuts to full names
        shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}
        # Convert shortcuts(keys) to full names(values) if it exists in the shortcuts dictionary. If not, keep the original input(2nd player_input) for validation.
        player_input = shortcuts.get(player_input, player_input)
        if player_input in ["rock", "paper", "scissors", "quit"]:
            return player_input
        print("Invalid choice. Please try again.") 

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "Player wins!"
    else:
        return "Computer wins!"


def run_gui_game():
    root = tk.Tk()
    root.title("Rock Paper Scissors")
    root.resizable(False, False)

    score = {"player": 0, "computer": 0, "ties": 0, "rounds": 0}

    header = tk.Label(root, text="Choose your move:")
    header.pack(padx=12, pady=(12, 6))

    result_label = tk.Label(root, text="", fg="blue")
    result_label.pack(padx=12, pady=6)

    round_label = tk.Label(root, text="Round 0")
    round_label.pack(padx=12, pady=(0, 6))

    score_label = tk.Label(root, text="Player 0 - Computer 0 (Ties 0)")
    score_label.pack(padx=12, pady=(0, 4))

    win_rate_label = tk.Label(root, text="Win %: Player 0.0% | Computer 0.0% | Ties 0.0%")
    win_rate_label.pack(padx=12, pady=(0, 6))

    scoreboard_frame = tk.Frame(root)
    scoreboard_frame.pack(padx=12, pady=(0, 12))

    scoreboard_title = tk.Label(scoreboard_frame, text="Scoreboard (per round)")
    scoreboard_title.pack(anchor="w")

    scoreboard_list = tk.Listbox(scoreboard_frame, width=52, height=6)
    scoreboard_list.pack()

    def update_score_label():
        """Update the score display and win rate percentages."""
        # Update score counter display
        score_label.config(
            text=f"Player {score['player']} - Computer {score['computer']} (Ties {score['ties']})"
        )
        
        # Calculate win rate percentages
        total_rounds = score["rounds"]
        if total_rounds > 0:
            player_pct = (score["player"] / total_rounds) * 100
            computer_pct = (score["computer"] / total_rounds) * 100
            tie_pct = (score["ties"] / total_rounds) * 100
        else:
            player_pct = computer_pct = tie_pct = 0.0
        
        # Update win rate display
        win_rate_label.config(
            text=f"Win %: Player {player_pct:.1f}% | Computer {computer_pct:.1f}% | Ties {tie_pct:.1f}%"
        )

    def play_round(player_choice):
        computer_choice = get_computer_choice()
        outcome = determine_winner(player_choice, computer_choice)

        score["rounds"] += 1

        if outcome == "Player wins!":
            score["player"] += 1
        elif outcome == "Computer wins!":
            score["computer"] += 1
        else:
            score["ties"] += 1

        result_label.config(
            text=f"You: {player_choice} | Computer: {computer_choice} -> {outcome}"
        )
        round_label.config(text=f"Round {score['rounds']}")
        update_score_label()

        scoreboard_list.insert(
            tk.END,
            (
                f"Round {score['rounds']}: You {player_choice}, Computer {computer_choice} -> {outcome} "
                f"| Totals: P{score['player']} C{score['computer']} T{score['ties']}"
            ),
        )
        scoreboard_list.yview(tk.END)

    button_frame = tk.Frame(root)
    button_frame.pack(padx=12, pady=(0, 12))

    tk.Button(button_frame, text="Rock ✊", width=10, command=lambda: play_round("rock")).grid(
        row=0, column=0, padx=4
    )
    tk.Button(button_frame, text="Paper 📄", width=10, command=lambda: play_round("paper")).grid(
        row=0, column=1, padx=4
    )
    tk.Button(
        button_frame, text="Scissors ✂️", width=10, command=lambda: play_round("scissors")
    ).grid(row=0, column=2, padx=4)

    tk.Button(root, text="Quit", width=10, command=root.destroy).pack(pady=(0, 12))

    root.mainloop()


if __name__ == "__main__":
    run_gui_game()
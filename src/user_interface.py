# Handles user interaction, including input prompts and displaying results.

from game_engine import GameAction

def get_user_action():
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    
    while True:
        user_input = input(f"\nPick a choice ({game_choices_str}): ")
        try:
            user_selection = int(user_input)
            if user_selection in range(len(GameAction)): return GameAction(user_selection)
            else: print(f"Invalid selection. Pick a choice in range [0, {len(GameAction) - 1}]!")
        except ValueError: print(f"Invalid input. Please enter a number between 0 and {len(GameAction) - 1}.")

def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'
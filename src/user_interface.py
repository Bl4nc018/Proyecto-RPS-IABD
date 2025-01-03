# Handles user interaction, including input prompts and displaying results.

from game_engine import GameAction

def get_user_action():
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action

def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'
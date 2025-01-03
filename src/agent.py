# Contains the logic for the computer agent's decision-making strategy.

import random
from game_engine import GameAction

def get_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")

    return computer_action

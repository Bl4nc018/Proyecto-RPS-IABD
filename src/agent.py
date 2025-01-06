# Contains the logic for the computer agent's decision-making strategy.

import random
from game_engine import GameAction

user_history = []  # Internal model used to track the user's last 20 actions

def get_computer_action(): 
    # This function determines the computer's action based on the user's action history. 
    # If the history is insufficient, it selects a random action.
    
    if len(user_history) < 5: computer_selection = random.randint(0, len(GameAction) - 1)
    else:
        most_common_action = max(set(user_history), key=user_history.count) # Obtains the most frequent action from the last 20 entries.
        counter_actions = { # Dictionary filled with counteractions for each possible user action.
            GameAction.Rock: [GameAction.Paper, GameAction.Spock],
            GameAction.Paper: [GameAction.Scissors, GameAction.Lizard],
            GameAction.Scissors: [GameAction.Rock, GameAction.Spock],
            GameAction.Lizard: [GameAction.Rock, GameAction.Scissors],
            GameAction.Spock: [GameAction.Paper, GameAction.Lizard],}
        
        # Now the variable selects a random counteraction from the available options.
        computer_selection = random.choice(counter_actions[most_common_action]).value

    computer_action = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")
    return computer_action


def update_user_history(user_action): 
    # This function updates the user's action history with their latest move. 
    # Keeps it limited to the last 20 actions for efficiency.
    
    user_history.append(user_action)
    if len(user_history) > 20: user_history.pop(0)
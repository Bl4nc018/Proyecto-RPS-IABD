# Implements the rules and logic for evaluating the game's outcome.

from enum import IntEnum

class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    # Added Lizard and Spock game actions for the extension.
    Lizard = 3
    Spock = 4

class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2

Victories = { # Updated with the Lizard, Spock extension.
    GameAction.Rock: [GameAction.Scissors, GameAction.Lizard],
    GameAction.Paper: [GameAction.Rock, GameAction.Spock],
    GameAction.Scissors: [GameAction.Paper, GameAction.Lizard],
    GameAction.Lizard: [GameAction.Spock, GameAction.Paper],
    GameAction.Spock: [GameAction.Scissors, GameAction.Rock], }

def assess_game(user_action, computer_action):
    game_result = None

    action_messages = { # Defined specific messages for each winning scenario so the if statements dont get complicated.
        (GameAction.Rock, GameAction.Scissors): "Rock smashes Scissors",
        (GameAction.Rock, GameAction.Lizard): "Rock crushes Lizard",
        (GameAction.Paper, GameAction.Rock): "Paper covers Rock",
        (GameAction.Paper, GameAction.Spock): "Paper disproves Spock",
        (GameAction.Scissors, GameAction.Paper): "Scissors cuts Paper",
        (GameAction.Scissors, GameAction.Lizard): "Scissors decapitates Lizard",
        (GameAction.Lizard, GameAction.Spock): "Lizard poisons Spock",
        (GameAction.Lizard, GameAction.Paper): "Lizard eats Paper",
        (GameAction.Spock, GameAction.Scissors): "Spock vaporizes Scissors",
        (GameAction.Spock, GameAction.Rock): "Spock smashes Rock",}

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. It's a Draw!")
        game_result = GameResult.Tie
    elif (user_action, computer_action) in action_messages:
        print(f"{action_messages[(user_action, computer_action)]}. You won!")
        game_result = GameResult.Victory
    else:
        print(f"{computer_action.name} beats {user_action.name}. You lost!")
        game_result = GameResult.Defeat

    return game_result


# Tests the rules and logic defined in the game engine.

import pytest
from src.game_engine import GameAction, GameResult, assess_game

# Added pytest's parameterized test feature to be able to test multiple scenarios for the assess_game function.
@pytest.mark.parametrize("user_action, computer_action, expected_result", [
    # Scenarios where the game ends in a tie:
    (GameAction.Rock, GameAction.Rock, GameResult.Tie),
    (GameAction.Paper, GameAction.Paper, GameResult.Tie),
    (GameAction.Scissors, GameAction.Scissors, GameResult.Tie),
    (GameAction.Lizard, GameAction.Lizard, GameResult.Tie),
    (GameAction.Spock, GameAction.Spock, GameResult.Tie),

    # Scenarios where the user wins:
    (GameAction.Rock, GameAction.Scissors, GameResult.Victory),
    (GameAction.Rock, GameAction.Lizard, GameResult.Victory),
    (GameAction.Paper, GameAction.Rock, GameResult.Victory),
    (GameAction.Paper, GameAction.Spock, GameResult.Victory),
    (GameAction.Scissors, GameAction.Paper, GameResult.Victory),
    (GameAction.Scissors, GameAction.Lizard, GameResult.Victory),
    (GameAction.Lizard, GameAction.Spock, GameResult.Victory),
    (GameAction.Lizard, GameAction.Paper, GameResult.Victory),
    (GameAction.Spock, GameAction.Scissors, GameResult.Victory),
    (GameAction.Spock, GameAction.Rock, GameResult.Victory),

    # Scenarios where the user loses:
    (GameAction.Rock, GameAction.Paper, GameResult.Defeat),
    (GameAction.Rock, GameAction.Spock, GameResult.Defeat),
    (GameAction.Paper, GameAction.Scissors, GameResult.Defeat),
    (GameAction.Paper, GameAction.Lizard, GameResult.Defeat),
    (GameAction.Scissors, GameAction.Rock, GameResult.Defeat),
    (GameAction.Scissors, GameAction.Spock, GameResult.Defeat),
    (GameAction.Lizard, GameAction.Rock, GameResult.Defeat),
    (GameAction.Lizard, GameAction.Scissors, GameResult.Defeat),
    (GameAction.Spock, GameAction.Paper, GameResult.Defeat),
    (GameAction.Spock, GameAction.Lizard, GameResult.Defeat),
])

def test_assess_game(user_action, computer_action, expected_result): # Tests all possible outcomes of the game.
    result = assess_game(user_action, computer_action)
    assert result == expected_result
# Tests the functionality of the computer agent's decision-making logic.
from src.agent import get_computer_action, update_user_history, user_history
from src.game_engine import GameAction

def test_update_user_history(): # Tests if the user history updates correctly.
    user_history.clear()
    update_user_history(GameAction.Rock)
    assert user_history == [GameAction.Rock]

    for _ in range(20):
        update_user_history(GameAction.Paper)
    assert len(user_history) == 20
    assert user_history[-1] == GameAction.Paper

def test_get_computer_action_random(): # Tests  if the agent makes a random choice with insufficient history.
    user_history.clear()
    action = get_computer_action()
    assert action in list(GameAction)

def test_get_computer_action_predictive(): # Tests if the agent predicts correctly based on history.
    user_history.clear()
    user_history.extend([GameAction.Rock] * 20)
    action = get_computer_action() # The agent should counter Rock with Paper or Spock
    assert action in [GameAction.Paper, GameAction.Spock]

def test_get_computer_action_with_mixed_history(): # Tests if the agent handles mixed user actions correctly.
    user_history.clear()
    user_history.extend([GameAction.Paper] * 10 + [GameAction.Scissors] * 10)
    action = get_computer_action() # The agent should counter Paper and Scissors
    assert action in [GameAction.Scissors, GameAction.Rock, GameAction.Lizard, GameAction.Spock]


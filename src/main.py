# Entry point of the program; coordinates the game flow.

from agent import get_computer_action
from game_engine import assess_game, GameAction
from user_interface import get_user_action, play_another_round


def main():
    while True:
        try: user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action()
        assess_game(user_action, computer_action)

        if not play_another_round(): break


if __name__ == "__main__":
    main()

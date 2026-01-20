# Console-based Rock–Paper–Scissors game demonstrating modular design, input validation, and rule-based game logic.

import sys, random


def main():
    welcome()

    wins = 0
    ties = 0
    losses = 0

    win_rules = {
        "r": "s",
        "p": "r",
        "s": "p"
    }

    while True:         # the main game loop
        results_tracker(wins, ties, losses)
        player_move = get_player_move()
        player_move_display(player_move)
        computer_move = get_computer_move()
        display_computer_move(computer_move)

        if player_move == computer_move:
            ties += 1
            print("It is a tie!")
        elif win_rules[player_move] == computer_move:
            wins += 1
            print("You win :)")
        else:
            losses += 1
            print("You lose :(")


def welcome():
    print_separator()
    print("*************** GAME: ROCK - PAPER - SCISSORS ***************")
    print_separator()
    print()


def print_separator():
    print("*" * 61)


def results_tracker(wins, ties, losses):
    print(f"************* Wins: {wins} *** Ties: {ties} *** Losses: {losses} *************")
    print_separator()
    print()


def instructions():
    print("****** Enter your move: (r)ock, (p)aper or (s)cissors ******")
    print("******************* For EXIT enter (q)uit ******************")
    print()


def invalid_command():
    print("******************* Invalid command ******************")


def game_over():
    print_separator()
    print("************************* GAME OVER *************************")
    print_separator()


def get_computer_move():
    """
    Randomly generates computer's response.
    """
    computer_move = random.choice(["r", "p", "s"])
    return computer_move


def display_computer_move(computer_move):
    """
    Displays on the screen computer's response.
    """
    if computer_move == "r":
        print("ROCK")
    elif computer_move == "p":
        print("PAPER")
    else:
        print("SCISSORS")


def get_player_move():
    """
    Prompts the player to enter a valid move.
    Returns: str: 'r', 'p', or 's' depending on the player's choice.
    Exits the game if the player enters 'q'.
    """
    while True:  # player prompts loop
        instructions()
        valid_input = {"r", "p", "s", "q"}
        player_move = input()

        if player_move not in valid_input:
            invalid_command()
        else:
            if player_move == "q":
                game_over()
                sys.exit()
            else:
                break
    return player_move


def player_move_display(player_move):
    """
    Displays on the screen player's choice.
    """
    if player_move == "r":
        print("ROCK versus...")
    elif player_move == "p":
        print("PAPER versus...")
    elif player_move == "s":
        print("SCISSORS versus")


if __name__ == "__main__":
    main()

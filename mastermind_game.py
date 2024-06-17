import random

def get_feedback(secret, guess):
    correct_position = sum(s == g for s, g in zip(secret, guess))
    correct_digits = sum(min(secret.count(d), guess.count(d)) for d in set(guess))
    return correct_position, correct_digits - correct_position

def play_round(secret, player_name):
    attempts = 0
    while True:
        guess = input(f"{player_name}, enter your guess: ")
        attempts += 1
        if guess == secret:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            return attempts
        else:
            correct_position, correct_digits = get_feedback(secret, guess)
            print(f"Digits in the correct position: {correct_position}, Correct digits but wrong position: {correct_digits}")

def mastermind_game():
    secret1 = input("Player 1, set a number: ")
    print("\nPlayer 2's turn to guess.")
    attempts_player2 = play_round(secret1, "Player 2")

    secret2 = input("\nPlayer 2, set a multi-digit number: ")
    print("\nPlayer 1's turn to guess.")
    attempts_player1 = play_round(secret2, "Player 1")
    
    if attempts_player1 < attempts_player2:
        print("\nPlayer 1 wins and is crowned Mastermind!")
    elif attempts_player1 > attempts_player2:
        print("\nPlayer 2 wins and is crowned Mastermind!")
    else:
        print("\nIt's a tie! Both players are equally Mastermind!")


mastermind_game()

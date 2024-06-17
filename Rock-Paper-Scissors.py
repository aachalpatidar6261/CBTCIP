def get_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors Game!")
    print("Winning Rules as follows:\nRock vs paper -> paper wins\nRock vs scissor -> rock wins\nPaper vs scissor -> scissor wins.\n")

    while True:
        player1_choice = input("Player 1, enter your choice (rock/paper/scissors): ").lower()
        player2_choice = input("Player 2, enter your choice (rock/paper/scissors): ").lower()

        if player1_choice not in ["rock", "paper", "scissors"] or player2_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        result = get_winner(player1_choice, player2_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thank you for playing!")


rock_paper_scissors()

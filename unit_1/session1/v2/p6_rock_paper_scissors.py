def rock_paper_scissors(player1, player2):
    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock" and player2 == "scissors":
        print("Player 1 wins!")
    elif player1 == "scissors" and player2 == "paper":
        print("Player 1 wins!")
    elif player1 == "paper" and player2 == "rock":
        print("Player 1 wins!")
    else:
        print("Player 2 wins")

rock_paper_scissors("rock", "rock")
rock_paper_scissors("scissors", "rock")
rock_paper_scissors("scissors", "paper")
rock_paper_scissors("rock", "paper")
rock_paper_scissors("paper", "rock")


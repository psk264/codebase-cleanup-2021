
from _typeshed import NoneType
from random import choice

#
# USER SELECTION
#

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in ["rock", "paper", "scissors"]:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(["rock", "paper", "scissors"])
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

def determine_winner(u, c):
    if u == "rock" and c == "rock":
        # print("It's a tie!")
        return None
    elif u == "rock" and c == "paper":
        # print("The computer wins")
        return c
    elif u == "rock" and c == "scissors":
        # print("The user wins")
        return u

    elif u == "paper" and c == "rock":
        # print("The computer wins")
        return c
    elif u == "paper" and c == "paper":
        # print("It's a tie!")
        return None
    elif u == "paper" and c == "scissors":
        # print("The user wins")
        return u

    elif u == "scissors" and c == "rock":
        # print("The computer wins")
        return c
    elif u == "scissors" and c == "paper":
        # print("The user wins")
        return u
    elif u == "scissors" and c == "scissors":
        # print("It's a tie!")
        return None

winner = determine_winner(u,c)

    #Refactoring
if winner == u:
    print("YOU won")
elif winner == c:
    print("COMP won")
else:
    print("Tie")
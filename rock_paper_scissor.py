import random

bot = ["rock", "paper", "scissors"]
bot_Choice = bot[random.randint(0, 2)]
player = False

while player == False:
    player = input("Let's play rock-paper-scissor! Pick rock, paper or scissors.")

if player == bot_Choice:
    print("Tie")

elif player == "rock":
    if bot_Choice == "paper":
        print("Loss. Paper beats rock.")
    else:
        print("Win. Rock beats scissors.")

elif player == "paper":
    if bot_Choice == "scissors":
        print("Loss. Scissors beat paper.")
    else:
        print("Win. Paper beats rock.")

elif player == "scissors.":
    if bot_Choice == "rock":
        print("Loss. Rock beats scissors.")
    else:
        print("Win. Scissors beat paper.")

else:
    print('That was not a valid statement. Hope you are not trying to cheat!')

#---------------ROCK , PAPER & SCISSORS GAME----------------------
import random
moves = ["rock","paper","scissors"]
print("WELCOME!!\nP.S: Take care of your spelling")
while True:
    computer = moves[random.randint(0,2)]
    player = input("rock, paper or scissors?\nTo end the game press 'quit' \n ")
    if player == "quit":
        print("The game has ended!")
        break
    elif player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer , "beats", player)
        else:
            print("You Win!", player, "beats", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "beats", player)
        else:
            print("You Win!", player, "beats", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose!", computer, "beats", player)
        else:
            print("You Win!", player, "beats", computer)
    else:
        print("Please check your spelling!")
   # break     #use this if you want to play game only at a once
import random

options=("rock", "paper", "scissor")
running=True

while running:
    player=None
    computer=random.choice(options)

    while player not in options:
        player=input("Enter choice (Rock,Paper,Scissor): \n")
    print(f"Player: {player}")
    print(f"Computer {computer}")


    if player==computer:
        print("Its a Tie!")

    elif player=="rock" and computer=="scissor":
        print("You WON!!")
    
    elif player=="paper" and computer=="rock":
        print("YOu WON!!")

    elif player=="scissor" and computer=="paper":
        print("You WON!!")
    
    else:
        print("You Lose!")

    if not input("Play Again?(y/n): \n").lower=="y":
        running=True
    print("Thanks For Playing")
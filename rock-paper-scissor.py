# a simple rock paper scissor game... enjoy!
import random
x=random.randint(1,3)

if x==1:
    x="rock"
elif x==2:
    x="paper"
else:
    x="scissor"

human_wins=0
computer_wins=0
ties=0

human=input("rock paper scissor SHOOT!!! ")
print(f"the computer chose {x}!!!")



if human == "rock" and x=="rock":
    print("its a tie")
    ties+=1

elif human=="rock" and x=="paper":
    print("computer wins")
    computer_wins+=1

elif human=="rock" and x=="scissor":
    print("human wins")
    human_wins+=1

elif human=="paper" and x=="rock":
    print("human wins")
    human_wins+=1

elif human=="paper" and x=="paper":
    print("its a tie")
    ties+=1

elif human=="paper" and x=="scissor":
    print("computer wins")
    computer_wins+=1

elif human=="scissor" and x=="rock":
    print("computer wins")
    computer_wins+=1

elif human=="scissor" and x=="paper":
    print("human wins")
    human_wins+=1

elif human=="scissor" and x=="scissor":
    print("its a tie")
    ties+=1

else:
    print("invalid input")


print(f"human wins: {human_wins},    computer wins:{computer_wins},     ties:{ties}")

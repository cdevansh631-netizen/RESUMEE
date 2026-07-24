import random
print("WELCOME TO ROCK PAPER GAME--")
l=["rock","paper","scissor"]
num=random.choice(l)
choice=input("ENTER YOUR(rock,paper,scissor) :")
if choice==num:
    print("DRAW OCCUR--")
elif choice=="rock" and num=="Scissor":
    print("you Won--")
elif choice=="paper" and num=="rock":
    print("You Won--")
elif choice=="Scissor" and num=="paper":
    print("You won--")
else:
    print("You lost--")
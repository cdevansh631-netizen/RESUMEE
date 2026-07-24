#NUMBER GUISSING GAME :--[THIS CODE HAVING A max_attempt LIMIT---]

import random
print("-WELCOME TO OUR NUMBER GUISIING GAME-")

# number=random.randint(1,100)
# attempt=0
# max_attempt=5

# while attempt<max_attempt:
#     guess=int(input("Guess No : "))
#     attempt+=1

#     if guess==number:
#         print("---WON---")
#         break
#     elif guess<number:
#         print("---TO LOW---")
#     else:
#         print("---TO HIGH---")


# if attempt==max_attempt and  number!=guess:
#     print("UUUU LOST HONEY...")


#NUMBER GUISIING GAME BUT WITH NO ATTEMPT LIMIT:

import random

print("Welcome to our number gussing game without any limit")


number=random.randint(1,10)
attempt=0

while True:
    guess=int(input("Guess Number : "))
    attempt+=1

    if guess<number:
        print("TO LOW HONEYYY")
    elif guess>number:
        print("TO HIGH HONEY")
    else:
        print("You Guess is Correct in ",attempt," attempt")
5








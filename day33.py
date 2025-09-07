#Number Guess Game
import random
playerName=input("Enter Your Name:")
print("You Have to Guess the number between 10 to 60")
print("Lets Start!!")
res=random.randint(10,60)
for i in range(1,6):
    print("*"*20)
    print("Round : ",i)
    guess=int(input("Guess the Number:"))
    if guess==res:
        print(playerName,"Guessed Actual Number")
        print(playerName,"Wins!!")
        break
    elif guess>res:
        print("Actual Number is Smaller than your Guess")
    elif guess<res:
        print("Actual Number is Greater tha your Guess")
    print("*"*20)
else:
    print(playerName,"Loose, reopen the game to play again")
    print("Actual Number is",res)

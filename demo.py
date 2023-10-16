import os
os.system('cls')
import random
snum=random.randint(1,100)
attempts=0
print("welcome to the guessing game")
print("I'm thinking of a number between 1 and 100")
while True:
    guess=int(input("your guess: "))
    attempts +=1
    if guess==snum:
        print(f"congratulation! your guessed the number {snum} in {attempts} attempts.")
        break
    elif guess<snum:
        print("try a higher number")
    else:
        print("try a lower number")
    
    
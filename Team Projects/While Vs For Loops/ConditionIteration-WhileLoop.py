#Number Guess Loop - Conditional Iteration
print("Guess a number between 0 and 10")

# Using a random number variable for the number
import random
num = random.randint(0,10)

guess = int(input("Guess a number: "))

#While Loop Ver.
while guess != num:
    guess = int(input("Try another number! "))

print("Congrats, you guessed the number!")


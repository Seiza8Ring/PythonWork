#Task 5: Number Guessing Game

print("Guess a number between 1 and 50.")

import random
num = random.randint(1,50)
guess = input
count = 1

while guess != num:
    guess = int(input("Your Guess: "))
    if guess > num:
        print("Too High!")
        count += 1
    elif guess < num:
        print("Too Low")
        count += 1
    else: break
print(f"Congrats! You got it in {count} guesses.")

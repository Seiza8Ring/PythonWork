#varible
guess = int(input("Guess a number 1 through 10 within 6 tries:"))

#pyhton grabs and chooses a number between 0 and 10
import random
number = random.randint(0, 5)

# if the guess is = to random number it then stops the loop
for i in range(5):
    guess = int(input("Guess a number 1 through 10:"))
    if guess == number: print(f"You guessed the right numnber!")
    #breaks the for loop after correctly guessing the random number
    if guess == number: break
#if the guess is not = to the generated number, you then failed
if guess != number:
    print(f"you failed to guess the number in {i+2} tries")



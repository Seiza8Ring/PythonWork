#Task 3: Random Number Guesser
print('Think of a number between 1 and 100...')
import random
guess = random.randint(1,100)
save = guess
count = 1
_match = False
numRange = input(f'My guess is {guess}. (higher/lower/correct): ')

while not _match:

    if numRange == 'higher':
        guess = random.randint(save,100)
        save = guess
        count += 1
        numRange = input(f'My guess is {guess}. (higher/lower/correct): ')
    elif numRange == 'lower':
        guess = random.randint(1,save)
        save = guess
        count += 1
        numRange = input(f'My guess is {guess}. (higher/lower/correct): ')
    elif numRange == 'correct':
        print(f'I got it in {count} guesses!')
        _match = True
    else:
        print('Something went wrong. Lets Retry That:')
        numRange = input(f'My guess is {guess}. (higher/lower/correct): ')

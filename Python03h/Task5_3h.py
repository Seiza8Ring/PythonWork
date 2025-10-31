#Task 5: Higher or Lower Game
import random
is_end = input
endGame = False
num = random.randint(1,100)
save = num
win = 0
loss = 0

while endGame == False:
    print(f'Current Number: {num}')
    num = random.randint(1,100)
    guess = input("Will the next number be (h)igher or (l)ower? ")
    print(f"Next Number: {num}")
    
    if guess == 'h' and num > save:
        print('You win!')
        win += 1
    elif guess == 'h' and save > num:
        print('You lose!')
        loss += 1
    elif guess == 'l' and save > num:
        print('You win!')
        win += 1
    elif guess == 'l' and num > save:
        print('You lose!')
        loss += 1
# Save the number for next round
    save = num
# End the game
    is_end = input("""
End Game? (y/n): """)

    if is_end == 'y':
        print(f'''
Wins: {win}
Losses: {loss}
''')
        endGame = True

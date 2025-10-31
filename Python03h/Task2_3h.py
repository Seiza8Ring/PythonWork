#Task 2: Coin Flip Simulator
import random
print('Flipping a coin 20 times...')
h = 0
t = 0

for i in range(20):
    coin = random.randint(0,1)
    if coin == 1:
        print('T', end=' ')
        t +=1
    elif coin == 0:
        print('H', end=' ')
        h +=1

print(f'''
Heads: {h}
Tails: {t}
''')

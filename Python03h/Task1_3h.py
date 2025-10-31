#Task 1: Dice Roller
import random
print('Rolling die 10 times:')
for i in range(10):
    roll = random.randint(1, 6)
    
    print(roll, end=' ')


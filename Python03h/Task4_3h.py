#Task 4: Lottery Number Generator
import random
lotnum = []

while len(lotnum) != 6:
    num = random.randint(1,49)
    if num not in lotnum:
        lotnum.append(num)
    elif num in lotnum:
        num = random.randint(1,49)
print(f'Your Lottery Numbers: {lotnum}')

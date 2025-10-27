import random
rolls = int(input("How many rolls?: "))
rollCount = 0
adver = 0
for i in range(rolls):
    roll = random.randint(1, 6)
    rollCount += 1
    adver += roll
    print(f"Die {i+1}: {roll}")
adverage = adver/rolls
print(f"Adverage roll: {adverage}")

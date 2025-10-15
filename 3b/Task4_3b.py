# Task 4: Sum Calculator
num = int(input("Enter a number: "))

total = 0
for i in range(0, num+1):
    total += i
print(f"The Sum of number 1 to {num} is {total}")

# Task 4: Factorial Calculator
num = int(input("Enter a number: "))

prdct = 1

for i in range(1, num + 1):
    prdct *= i

print(f"The factorial of {num} is {prdct}")

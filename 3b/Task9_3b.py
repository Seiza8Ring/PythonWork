# Task 9: Average Calculator
count = int(input("How many numbers? "))
total = 0
for i in range(count):
    num = int(input(f"Enter number {i+1}: "))
    total += num
adverage = total / count

print(f"The adverage is {adverage}")

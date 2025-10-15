# Task 6: Range Calculator
low = int(input("Enter lower bound: "))
high = int(input("Enter upper bound: "))

total = 0
for i in range(low,high+1):
    total += i
print(f"The sum of numbers from {low} to {high} is {total}")

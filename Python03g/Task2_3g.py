#Task 2: Sum Until Zero
num = int
numSum = 0
while num != 0:
    num = int(input("Enter a number (0 to stop): "))
    numSum += num
print(f"Total sum: {numSum}")

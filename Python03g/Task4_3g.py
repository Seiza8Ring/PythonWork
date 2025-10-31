#Task 4: Average Calculator
num = input
total = 0
count = 0

while num != -1:
    num = int(input("Enter a number: "))
    if num != -1:
        total += num
        count += 1

adver = total / count
print(f"Adverage: {adver:.2f}")

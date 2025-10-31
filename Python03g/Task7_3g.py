#Task 7: Factorial Calculator
num = int(input("Enter a number: "))
product = 1
count = 1

while count <= num:
    product *= count
    count += 1
print(f'{num}! = {product}')

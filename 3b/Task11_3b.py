# Bonus Challenge: Prime Number Checker
num = int(input("Enter a number: "))
is_prime = 2
if num <= 1:
    is_prime = 2
    
for i in range(2,num):
    if num % i == 0:
        is_prime = 1
    else:
        is_prime = 0
        
if is_prime == 1:
    print(f"{num} is not a prime number")
elif is_prime == 0:
    print(f"{num} is a prime number")
else: print("ERROR")

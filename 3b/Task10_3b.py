# Challenge Task: Fibonacci Sequence
fibNum = int(input("How many Fibonacci numbers? "))

a = 0
b = 1
for i in range(1,fibNum+1):
    print(a, end=" ")
    nextNum = a + b
    a = b
    b = nextNum
    

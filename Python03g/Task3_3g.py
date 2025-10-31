#Task 3: Password Validator
password = 'python123'
inputKey = input

while inputKey != password:
    inputKey = input("Enter password: ")
    if inputKey != password: print("Incorrect! Try again.")
    
print("**Welcome User**")

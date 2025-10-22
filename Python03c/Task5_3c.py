#Task 5: Reverse String Builder
string = input("Enter Text: ")
reverse = ''
#string notation
for i in string[::-1]:
    reverse += i
print(reverse)

#Task 6: Input Validation
grade = -1
check = False
#if check == False: g

while check == False:
    grade = int(input("Enter a grade: "))
    if 0 <= grade <= 100: check = True
    else: print("Invalid! Must be between 0 and 100.")

print(f'Valid Grade accepted: {grade}')

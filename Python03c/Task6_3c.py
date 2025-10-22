#Task 6: Report Card Generator
name = input("Enter Student Name: ")
subject = []
grade= []
total = 0
for i in range(0,5):
    subject.append(input("Enter Subject: "))
    grade.append(int(input("Enter Grade (#/100): ")))
    total += grade[i]

adverage = total/5
letter = 'X'
if adverage >= 90: letter = 'A'
elif adverage >= 80: letter = 'B'
elif adverage >= 70: letter = 'C'
elif adverage >= 60: letter = 'D'
else: letter = 'F'

print(f"""
***REPORT CARD***
Student Name: {name}
{subject[0]} grade is {grade[0]}
{subject[1]} grade is {grade[1]}
{subject[2]} grade is {grade[2]}
{subject[3]} grade is {grade[3]}
{subject[4]} grade is {grade[4]}

Adverage Grade: {adverage}
Letter Grade: {letter}
""")


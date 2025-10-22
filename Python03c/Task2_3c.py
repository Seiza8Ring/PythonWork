# Task 2: Letter Counter
text = input("Enter some text: ")
aCount = 0
for i in text:
    if i == 'a': aCount += 1

#make 'times' non-plural when there's only 1 'a'
if aCount == 1:
    is_plural = ''
else: is_plural = 's'

print(f"The letter 'a' appears {aCount} time{is_plural}")

#Task 3: Vowel and Consonant Counter
text = input("Enter Text: ")
vowels = 0
const = 0
for i in text:
    if i in "aeiouAEIOU":
        vowels += 1
    if i in "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM":
        const += 1

print(f'Vowels: {vowels}, Consonants: {const}')

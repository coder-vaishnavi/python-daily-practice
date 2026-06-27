# Write a program that counts how many vowels are in a given string.

text = input("Enter a string: ").lower()

count = (text.count('a') +
         text.count('e') +
         text.count('i') +
         text.count('o') +
         text.count('u'))

print("Number of vowels:", count)
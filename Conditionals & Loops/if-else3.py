#Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".
num = int(input("enter the num "))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
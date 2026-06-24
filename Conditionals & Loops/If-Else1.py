#Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
num = int(input("enter any number"))
if num>0:
    print(f"{num} is positive")
elif num<0:
    print(f"{num} is negative")
else:
    print(f"num is zero")
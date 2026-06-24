# Use a while loop to reverse a given number (e.g., 123 → 321).
# Python: / gives a decimal result, // gives an integer result (like Java's / for integers). 
num = int(input("enter any number"))
temp = num
rem = 0
rev = 0
while num !=0:
    rem = num%10
    rev = rev * 10 + rem
    num = num//10
print(f"reverse num of {temp} is {rev}")
    
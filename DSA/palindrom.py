x = int(input("enter a number"))
if x < 0:
    print("not palindrome")
temp = x
rev = 0

while x > 0:
    rem = x % 10
    rev = rev * 10 + rem
    x = x // 10
    
if temp == rev:
    print("palindrome")
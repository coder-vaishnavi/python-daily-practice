x = int(input("Enter an integer: "))

temp = x

# Make number positive if negative
if x < 0:
    x = -x

rev = 0

# Reverse the number
while x != 0:
    rem = x % 10
    rev = rev * 10 + rem
    x = x // 10

# Restore the sign
if temp < 0:
    rev = -rev

# Check 32-bit signed integer range
if rev < -2**31 or rev > 2**31 - 1:
    print(0)
else:
    print("Reversed Number:", rev)
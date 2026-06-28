# Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.
def safe_divide(a, b):
    if b==0:
        print("Cannot divide by zero")
    return a/b
print(f"division of a=6 and b=2 is {safe_divide(6,2)}")

# Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.

import my_utils

my_utils.is_even(8)
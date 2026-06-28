# Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.
# Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.

print("Q1")
def increament():
    counter = 0
    return counter + 1
print(increament())
print(increament())
print(increament())
print("dose not persists across function calls")

print("Q2")
def multiply(a, b):
    '''multiply function return the multiplication of two num

        take integer input a and b
        returns a*b
    '''
    return a*b
print(multiply(5,6))
print(multiply.__doc__)


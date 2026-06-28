# Write a function greet() that prints "Hello, Python Learner!" when called.
# Write a function square(num) that returns the square of a given number. Test it with different numbers.
def greet():
    print("Hello, python learner!") 

greet()

def square(num):
    return num*num
num = int(input("enter any no"))
print(f"square of {num} is {square(num)}")
# Q1:Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".

# Q2:Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width
# Only length (use default width)
def full_name(first, last):
    return f"full name is {first} {last}"

print(full_name("vaishnavi","deshmukh"))

def calculate_area(length, width=10):
    return f"returns the area of a rectangle of length:{length} and width:{width} is {length*width}"

print(calculate_area(length=10))
# Write a lambda function that adds two numbers and test it.
# Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.
sum = lambda a, b : a + b
print(f"lambda function that adds two numbers sum(10,3) is equal to {sum(10,3)}")

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(f"list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares {squares}")
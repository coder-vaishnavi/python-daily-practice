# Start with numbers = [5, 2, 9, 1, 7] and do the following:

# Sort the list in ascending order.
# Append the number 10 to the list.
# Remove the number 2 from the list.
numbers = [5, 2, 9, 1, 7]
print(f" before operations {numbers}")
numbers.sort()
print(f"Sort the list in ascending order {numbers}")
numbers.append(10)
print(f"after Append the number 10 to the list {numbers}")
numbers.remove(2)
print(f"after Remove the number 2 from the list {numbers}")
# Create a list names = ["Alice", "Bob", "Charlie"] and use the insert() method to add "David" at index 1.
names = ["Alice", "Bob", "Charlie"]
names.insert(1,"David")
print(f"after add 'David' at index 1 {names}")

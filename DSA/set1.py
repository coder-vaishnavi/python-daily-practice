# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)
my_set = {1, 2, 3, 3, 4}
print(f"set is {my_set}")
my_set.add(3)
print(f"set is after adding 3 {my_set}")
# Add 5 to the set, remove 2, and check if 4 is in the set.
my_set.add(5)
my_set.remove(2)
print(my_set)
# Create two sets:
a = {1, 2, 3}
b = {3, 4, 5}
print(f"a = {a} \nb= {b}")
# Find their:
# Union
print(f"a union b {a.union(b)}")
# Intersection
print(f"a interaction b {a.intersection(b)}")
# Difference (a - b)
print(f"a difference b {a.difference(b)}")
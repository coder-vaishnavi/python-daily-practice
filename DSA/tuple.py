# Create a tuple coordinates = (10, 20) and print both elements.
coordinates = (10, 20)
print(coordinates)
# Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
# coordinates[0] = 50
print(coordinates)
print(f"when I used to update value it says \n'coordinates[0] = 50 \nTypeError: 'tuple' object does not support item assignment'")
# Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.
coord_list = list(coordinates)
print(f"list is {coord_list}")
print(type(coordinates))
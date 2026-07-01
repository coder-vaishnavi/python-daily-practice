# Write a program that merges two dictionaries into one.
dict1 = {
    "vaishnavi": 30,
    "anisha": 40,
    "nita": 30
}

dict2 = {
    "city1": "Pune",
    "city2": "Satara",
    "city3": "Mumbai"
}

print("Before Merge")
print(dict1)
print(dict2)

dict1.update(dict2)

print("\nAfter Merge")
print(dict1)
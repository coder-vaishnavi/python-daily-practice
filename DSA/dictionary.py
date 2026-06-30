# Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:
student = {"name": "John", "age": 20, "grade": "A"}
# Print the value of "name".
print(f"the value of 'name': {student['name']}")
# Change "grade" to "A+".
student.update({"grade": "A+"})
print(f"after Change 'grade' to 'A+' {student}")
# Add a new key "city" with value "Delhi".
student["city"] = "Delhi"
print(student)
# Create a dictionary
friends = {
    "Vaishnavi": "9876543210",
    "Amit": "9123456789",
    "Sneha": "9988776655"
}

# Get all names (keys)
print("Names:", friends.keys())

# Get all phone numbers (values)
print("Phone Numbers:", friends.values())

# Loop through key-value pairs
print("\nFriends and their phone numbers:")
for name, number in friends.items():
    print(f"{name} : {number}")
#Write a program that keeps asking the user to enter a password until they enter the correct one.
password = ""

while password != "vaishnavi":
    password = input("Enter password: ")

    if password != "vaishnavi":
        print("Incorrect password. Try again.")

print("Password accepted!")
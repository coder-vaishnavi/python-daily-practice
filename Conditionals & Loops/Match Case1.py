# Step 1: Prompt the user to enter a day number and convert it to an integer
day_number = int(input("Enter a day number (1-7): "))

# Step 2: Use match-case to determine the corresponding day of the week
match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")

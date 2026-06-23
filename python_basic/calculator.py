a = int(input("enter any number"))
b = int(input("enter any number"))
print("1. addition\n2. subtraction\n3. division\n4. multiplication")
claculator = int(input("give operation to perform"))
match claculator:
    case 1:
        result = a+b
    case 2:
        result = a-b
    case 3:
        result = a/b
    case 4:
        result = a*b
    case _:
        print("invalid operation")
print(result)
s = input("Enter the string: ")
part = input("Enter the substring: ")

while part in s:
    index = s.find(part)
    s = s.replace(part,"",1)

print("Result:", s)
# Reverse a list without using reverse() or slicing ([::-1]).
n = int(input("Enter length of list: "))

num_list = []

for i in range(n):
    num_list.append(int(input("Enter element: ")))

reverse_list = []

for num in num_list:
    reverse_list.insert(0, num)

print("Original List:", num_list)
print("Reversed List:", reverse_list)
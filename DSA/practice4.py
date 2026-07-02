# ============================================
# Question:
# Reverse a list without using reverse() or slicing ([::-1]).
# ============================================

# Take input
n = int(input("Enter length of list: "))

num_list = []

for i in range(n):
    num_list.append(int(input("Enter element: ")))

print("\nOriginal List:", num_list)


# ============================================
# Method 1: Using for loop
# ============================================

reverse_list = []

for i in range(len(num_list) - 1, -1, -1):
    reverse_list.append(num_list[i])

print("\nMethod 1 (For Loop):", reverse_list)


# ============================================
# Method 2: Using while loop
# ============================================

reverse_list = []

i = len(num_list) - 1

while i >= 0:
    reverse_list.append(num_list[i])
    i -= 1

print("Method 2 (While Loop):", reverse_list)


# ============================================
# Method 3: Using insert()
# ============================================

reverse_list = []

for num in num_list:
    reverse_list.insert(0, num)

print("Method 3 (Insert):", reverse_list)


# ============================================
# Method 4: Using Two Pointers (Swapping)
# ============================================

swap_list = num_list.copy()

left = 0
right = len(swap_list) - 1

while left < right:
    swap_list[left], swap_list[right] = swap_list[right], swap_list[left]
    left += 1
    right -= 1

print("Method 4 (Swapping):", swap_list)


# ============================================
# Method 5: Using pop()
# ============================================

pop_list = num_list.copy()
reverse_list = []

while pop_list:
    reverse_list.append(pop_list.pop())

print("Method 5 (Pop):", reverse_list)
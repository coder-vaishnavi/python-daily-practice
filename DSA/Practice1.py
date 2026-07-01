# Write a program that takes a list of numbers and removes all duplicates using a set.
num = [1,2,3,4,3,2,5,6]
print(f"list is {num}")
#using variable
set_num = list(set(num))
print(f"after removing duplicates using set: {set_num}")
#without using variable
num = set(num)
print(num)
# Given an array nums containing n distinct numbers in the range [0, n], return the only number that is missing
n = int(input("enter length of list"))
list_set = []
for i in range(n):
    num = int(input("Enter numbers"))
    list_set.append(num)
hash_set = {}
miss_set = []
for i in range(len(list_set)):
    hash_set[list_set[i]] = i
for j in range(n+1):
    if j not in hash_set:
        miss_set.append(j)
print(hash_set) 
print(list_set)
print(miss_set)


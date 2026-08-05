nums = list(map(int, input("Enter the numbers: ").split()))

hash_list = {}

# Count frequency
for i in range(len(nums)):
    if nums[i] in hash_list:
        hash_list[nums[i]] += 1
    else:
        hash_list[nums[i]] = 1

# Store duplicates
num_list = []

for i in hash_list:
    if hash_list[i] > 1:
        num_list.append(i)

print("Duplicate elements:", num_list)
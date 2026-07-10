# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
# You may assume:
# Exactly one solution exists.
# You cannot use the same element twice.
nums = [2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)
# time complexity is On^2
#for time complexity O(n)
hash_map = {}
for i in range(len(nums)):
    sum = target - nums[i]
    if sum in hash_map:
        print(f"hash_map O(n) solution {hash_map[sum],i}")
    else:
        hash_map[nums[i]] = i
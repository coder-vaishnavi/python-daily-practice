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

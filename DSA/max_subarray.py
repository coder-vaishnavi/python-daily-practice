# Problem Statement
# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# that has the largest sum, and return its sum.
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = nums[0]
current_sum = nums[0]
for i in range(1, len(nums)):
    if nums[i] > current_sum + nums[i]:
        current_sum = nums[i]
    else:
        current_sum = current_sum + nums[i]
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)
# Given an array of integers nums, calculate the pivot index.
# The pivot index is the index where:
# Sum of all elements to the left = Sum of all elements to the right
# Return the leftmost pivot index.
# If none exists, return -1.
nums = [1,7,3,6,5,6]
index = 0
total_sum = 0
left_sum = 0
for i in range(len(nums)):
    total_sum = total_sum + nums[i]
for i in range(len(nums)):
    right_sum = total_sum - left_sum - nums[i]
    if left_sum == right_sum:
        print(i)
        break
    left_sum = left_sum + nums[i]
        
print(left_sum) 

# alternate solution
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         total_l = 0
#         total_r = sum(nums)

#         for idx, n in enumerate(nums):
#             total_r -= n

#             if total_l == total_r:
#                 return idx
            
#             total_l += n

#         return -1

    
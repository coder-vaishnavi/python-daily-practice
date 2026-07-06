# Given a list, rotate it left by one position.
# ❌ Don't use:
# pop()
# insert()
# Slicing ([:])
# Extra list
nums = [1, 2, 3, 4, 5]

first = nums[0]
for i in range(len(nums)-1):
    nums[i] = nums[i+1]

nums[-1] = first
print(nums)
    
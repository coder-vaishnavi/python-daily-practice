# Find the Second Largest Number
nums = [10, 25, 8, 40, 35]
largest = nums[0]
for i in range(len(nums)):
    if nums[i] >= largest:
        largest = nums[i]
second = float('-inf') #if list contains negative numbers:
print(nums)
for j in range(len(nums)):
    if nums[j]>= second and nums[j]!=largest:
        second = nums[j]
print("Largest:", largest)
print("Second Largest:", second)
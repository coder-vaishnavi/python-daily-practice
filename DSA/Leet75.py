# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.
nums = [2,0,2,1,1,0]
z = 0
o = 0
t = 0
for i in nums:
    if i == 0:
        z += 1
    elif i == 1:
        o += 1
    else:
        t += 1
for j in range(len(nums)):
    if j<z:
        nums[j] = 0
    elif z<=j<z+o:
        nums[j] = 1
    else:
        nums[j] = 2
print(nums)
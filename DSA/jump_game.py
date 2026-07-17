# Given an array nums, where nums[i] is the maximum jump length from index i, determine if you can reach the last index.
nums = [2,3,1,1,4]
jump = 0
farthest = 0 
for i in range(len(nums)):
    if i > farthest:
        print("not reachable")
        break
    new_reach = i + nums[i]
    if new_reach > farthest:
        farthest = new_reach
else:
    print("reached")

        
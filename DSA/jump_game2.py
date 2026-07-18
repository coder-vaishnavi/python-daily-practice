# You are given an array of non-negative integers nums, where each element represents the maximum jump length from that position.

# Return the minimum number of jumps required to reach the last index.

# You can always reach the last index.
nums = [2, 3, 1, 1, 4]

jumps = 0
current_end = 0
farthest = 0

for i in range(len(nums) - 1):

    new_reach = i + nums[i]

    if new_reach > farthest:
        farthest = new_reach

    if i == current_end:
        jumps += 1
        current_end = farthest

print(jumps)
nums = list(map(int, input("Enter the numbers: ").split()))

# Phase 1: Find meeting point
slow = nums[0]
fast = nums[0]

while True:
    slow = nums[slow]
    fast = nums[nums[fast]]

    if slow == fast:
        break

# Phase 2: Find duplicate
slow = nums[0]

while slow != fast:
    slow = nums[slow]
    fast = nums[fast]

print("Duplicate number is:", slow)
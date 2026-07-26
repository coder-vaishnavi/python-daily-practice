nums = [100, 4, 200, 1, 3, 2]

if len(nums) == 0:
    print(0)
else:
    nums.sort()

    count = 1
    max_count = 1

    for i in range(len(nums) - 1):

        # Ignore duplicates
        if nums[i] == nums[i + 1]:
            continue

        # Consecutive numbers
        elif nums[i + 1] - nums[i] == 1:
            count += 1
            max_count = max(max_count, count)

        # Sequence breaks
        else:
            count = 1
print("Longest Consecutive Sequence Length:", max_count)
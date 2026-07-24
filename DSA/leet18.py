nums = [1, 0, -1, 0, -2, 2]
target = 0

nums.sort()
n = len(nums)
result = []

# First number
for first in range(n - 3):
    if first > 0 and nums[first] == nums[first - 1]:
        continue

    # Second number
    for second in range(first + 1, n - 2):
        if second > first + 1 and nums[second] == nums[second - 1]:
            continue

        remaining_target = target - nums[first] - nums[second]

        left = second + 1
        right = n - 1

        # Two-pointer
        while left < right:
            current_sum = nums[left] + nums[right]

            if current_sum < remaining_target:
                left += 1

            elif current_sum > remaining_target:
                right -= 1

            else:
                result.append([
                    nums[first],
                    nums[second],
                    nums[left],
                    nums[right]
                ])

                # Skip duplicates
                left_value = nums[left]
                right_value = nums[right]

                while left < right and nums[left] == left_value:
                    left += 1

                while left < right and nums[right] == right_value:
                    right -= 1

print(result)
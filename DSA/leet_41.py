nums = list(map(int, input("Enter numbers: ").split()))

numsSet = set(nums)

for i in range(1, len(nums) + 1):
    if i not in numsSet:
        print("First missing positive:", i)
        break
else:
    print("First missing positive:", len(nums) + 1)
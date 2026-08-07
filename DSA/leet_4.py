nums1 = list(map(int, input("Enter nums1: ").split()))
nums2 = list(map(int, input("Enter nums2: ").split()))

for i in nums2:
    nums1.append(i)

nums1.sort()

if len(nums1) % 2 == 0:
    median = (nums1[len(nums1) // 2] + nums1[(len(nums1) // 2) - 1]) / 2
else:
    median = nums1[len(nums1) // 2]

print("Median:", median)
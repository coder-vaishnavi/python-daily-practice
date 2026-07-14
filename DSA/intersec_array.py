# Given two integer arrays nums1 and nums2, return an array of their intersection.

# Each element in the result must be unique, and you may return the result in any order.
nums1 = [1,2,2,1]
nums2 = [2,2]
inter_list = []
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] == nums2[j]:
            if nums1[i] not in inter_list:
                inter_list.append(nums1[i])
print(inter_list)

# using hashmap
# hash_set = set(nums1)
# inter_list = []
# for num in set(nums2):
#     if num in hash_set:
#         inter_list.append(num)

# print(inter_list)


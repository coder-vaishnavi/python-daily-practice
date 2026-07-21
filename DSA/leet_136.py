#single numberclass Solution:
nums = [2,2,1,4,3,4,3]
hash_list = {}
for i in range(len(nums)):
    if nums[i] in hash_list:
        hash_list[nums[i]] += 1
    else:
        hash_list[nums[i]] = 1
for j in range(len(nums)):
    if hash_list[nums[j]] == 1:
        print(nums[j])
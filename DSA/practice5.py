# Remove Duplicates from Sorted Array
nums = [0,0,1,1,1,2,2,3,3,4]
def return_unique_elements(nums):
    index = 1
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[index] = nums[i+1]
            index += 1
    print(nums)
    return index
print(f" unique elements are {return_unique_elements(nums)}")
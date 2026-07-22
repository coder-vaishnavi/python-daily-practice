height = [1,8,6,2,5,4,8,3,7]
# max_w = 0
# for i in range(len(height)):
#     for  j in range(i+1,len(height)):
#         w = j -i
#         ht = min(height[i],height[j])
#         area = w * ht
#         if area > max_w:
#             max_w = area
# print(max_w)

# optimal solution for O(n)
i = 0
j = len(height) - 1
max_w = 0
while i<j:
    w = j - i
    ht = min(height[i],height[j])
    c_w = w * ht
    max_w = max(c_w,max_w)
    if height[i] < height[j]:
        i += 1
    else:
        j -= 1
print(max_w)
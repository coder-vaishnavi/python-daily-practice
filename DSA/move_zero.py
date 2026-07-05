# Move All Zeros to the End
List = [0,1,0,3,12]
index = 0
for num in List:
    if num != 0:
        List[index] = num
        index += 1
# print(index)
for i in range(index,len(List)):
    List[i]= 0
print(List)
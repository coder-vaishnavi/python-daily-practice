grid = [[1,3],[2,2]]
i = 0
j = 0
n = len(grid)
hash_list = {}
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] in hash_list:    
            hash_list[grid[i][j]] += 1
        else:
            hash_list[grid[i][j]] = 1
    for num in range(1, n*n + 1):

        if hash_list.get(num, 0) == 0:
            ms = num

        if hash_list.get(num, 0) == 2:
            rp = num

print([rp,ms])
        

         

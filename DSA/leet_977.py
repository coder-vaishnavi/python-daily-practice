nums = list(map(int, input("Enter sorted array: ").split()))

sq = []

for i in nums:
    sq.append(i * i)

sq.sort()

print("Sorted squares:", sq)
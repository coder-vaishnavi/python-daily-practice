nums = list(map(int, input("Enter numbers: ").split()))

even = []
odd = []

for num in nums:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

result = even + odd

print("Sorted by parity:", result)
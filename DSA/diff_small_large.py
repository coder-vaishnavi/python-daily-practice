# Find the difference between the largest and smallest number.
List = [8, 15, 3, 22, 10]
def small_large_diff(List):
    small = List[0]
    for num in List:
        if num <= small:
            small = num
    print(small)
    large = List[0]
    for num in List:
        if num >= large:
            large = num
    print(large)
    return large-small

print(f"Find the difference between the largest and smallest number {small_large_diff(List)}")
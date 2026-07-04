# Find the Smallest Element
# ❌ Don't use min()
# ❌ Don't use sort()
List = [5,2,8,7,9]
def small(List):
    small = List[0]
    for num in List:
        if num <= small:
            small = num
        
    return small

print(f"small no is: {small(List)}")
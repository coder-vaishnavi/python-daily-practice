# Given two strings s and t, return true if t is an anagram of s, otherwise return false.
# An anagram means both strings contain the same characters with the same frequency, but possibly in a different order.
s = list(str(input("enter first string")))
t = list(str(input("enter second string")))

s_hash_map = {}
for num in s:
    if num in s_hash_map:
        s_hash_map[num] += 1
    else:
        s_hash_map[num] = 1
        
t_hash_map = {}
for num in t:
    if num in t_hash_map:
        t_hash_map[num] += 1
    else:
        t_hash_map[num] = 1

if s_hash_map == t_hash_map:
    print(True)
else:
    print(False)
    
    
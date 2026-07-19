# Assume you are assigning cookies to children.
# g[i] = greed factor of the i-th child (minimum cookie size they need)
# s[j] = size of the j-th cookie
# Each child can receive only one cookie, and each cookie can be used only once.
# Your goal is to maximize the number of satisfied children.
g = [1, 2, 3]
s = [1, 1]
g.sort()
s.sort()

i = 0
j = 0
count = 0

while i < len(g) and j < len(s):

    if g[i] <= s[j]:
        j+=1
        i+=1
        count+=1

    else:
        j+=1
print(count)
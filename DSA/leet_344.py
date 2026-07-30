
s = ["h","e","l","l","o"]
j = -1
var = ""
for i in range(len(s)//2):
    var = s[i]
    s[i] = s[j]
    s[j] = var
    j -=1
print(f"after reversing {s}")
        
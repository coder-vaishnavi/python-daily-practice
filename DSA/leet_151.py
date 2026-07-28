str_s = "I am Vaishnavi"
cl_s = " ".join(str_s.split())
r = list(cl_s.split(" "))
s = []
for i in range(len(r)-1,-1,-1):
    s.append(r[i])
print(" ".join(s))




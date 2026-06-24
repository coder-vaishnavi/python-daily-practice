# Print the following pattern using a for loop:
# *
# **
# ***
# ****
#end="" tells Python:
# "After printing, don't go to the next line."
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
s = input("Enter the brackets: ")

stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

valid = True

for ch in s:
    if ch in "([{":
        stack.append(ch)
    else:
        if not stack or stack[-1] != pairs[ch]:
            valid = False
            break
        stack.pop()

if valid and len(stack) == 0:
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")
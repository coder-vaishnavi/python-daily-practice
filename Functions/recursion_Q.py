# Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 6

for i in range(0,n+1):
    print(fibonacci(i), end=" ")
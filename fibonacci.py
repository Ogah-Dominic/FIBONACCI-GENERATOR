def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Test the function
num = 100
print(f"Fibonacci series up to {num}:")
for i in range(num):
    print(fibonacci_memo(i))
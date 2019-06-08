# cracking the code interview

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    elif n > 1:
        return memo.setdefault(n, fibonacci(n - 1) + fibonacci(n - 2))
    return n

print fibonacci(10)

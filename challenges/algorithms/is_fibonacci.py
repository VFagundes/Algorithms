import math


def is_perfect_square(n):
    sqr = int(math.sqrt(n))
    return sqr * sqr == n


def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


for i in range(10):
    print(i, str(is_fibonacci(i)))




print(is_fibonacci(6))
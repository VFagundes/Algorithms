def prime_numbers(n):
    primes = list()
    for y in xrange(1, n + 1):
        if all(y % i != 0 for i in range(2, int(y ** .5) + 1)):
            primes.append(y)
    return primes


"""
print prime_numbers(10)
print prime_numbers(100)
"""

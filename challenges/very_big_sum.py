import sys
import operator

def aVeryBigSum(n, ar):
    total = 0
    for i in ar:
        total+=i
    return reduce(operator.add,ar)

n = int(raw_input().strip())

ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)

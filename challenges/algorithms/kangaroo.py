import math


def solution(x1, v1, x2, v2):
    if v2 >= v1 and x1 != x2:
        return "NO"
    total = x1 + v1 + x2 + v2
    for i in range(total):
        x1 += v1
        x2 += v2
        if x2 == x1:
            return 'YES'
    return 'NO'


def solution2(x1, v1, x2, v2):
    if v2 >= v1 and x1 != x2:
        return "NO"
    else:
        x = float((x2 - x1) / (v1 - v2))

        if math.floor(x) == x:
            return "YES"
        else:
            return "NO"



# must be yes
print solution2(0, 3, 4, 2)

# must be no
print solution2(0, 2, 5, 3)
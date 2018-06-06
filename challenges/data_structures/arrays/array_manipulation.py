#https://www.hackerrank.com/challenges/crush/problem
n = 5
m = 3
data = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]]

def arrayManipulation(n, queries):
    arr = [0] * n
    for i in range(len(queries)):
        a, b, k = [queries[i][0], queries[i][1], queries[i][2]]
        arr[a - 1] += k
        if b <= (n - 1):
            arr[b] -= k
    total = x = 0
    for i in range(n):
        x += arr[i]
        if total < x:
            total = x
    return total


print arrayManipulation(n, data)

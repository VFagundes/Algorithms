from collections import deque

# default_array = default_data.get_default_array(0,5)
arr = [1, 2, 3, 4, 5]
n = len(arr)
d = 4


def rotate(n, d, arr):
    new_arr = deque()

    for i in range(0, d):
        new_arr.appendleft(arr[d - 1 - i])

    for i in range(0, n - d):
        new_arr.appendleft(arr[n - 1 - i])
    return new_arr


def rotate2(n, d, arr):
    new_arr = [None] * 5
    for i in range(0, n):
        new_arr[(i + n - d) % n] = arr[i]
    return new_arr


print ' '.join(map(str, rotate(n, d, arr)))
print '-----------------'
print ' '.join(map(str, rotate2(n, d, arr)))

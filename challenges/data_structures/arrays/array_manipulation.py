
N, M = [int(n) for n in raw_input().split()]
arr = [0] * N
for _ in range(M):
    a, b, k = [int(n) for n in raw_input().split()]
    arr[a - 1] += k
    if b <= (N - 1):
        arr[b] -= k
my_max = x = 0
for i in range(N):
    x += arr[i]
    if my_max < x:
        my_max = x

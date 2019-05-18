# 7
# 0 0 1 0 0 1 0
# Complete the jumpingOnClouds function below.
def jumping_on_clouds(c, n):
    count = -1
    i = 0
    while i < n:
        count += 1
        if i < n - 2 and c[i + 2] == 0:
            i += 2
            continue
        i += 1

    return count


c = [0, 0, 1, 0, 0, 1, 0]
n = len(c)

print(jumping_on_clouds(c, n))

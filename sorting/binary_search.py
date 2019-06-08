arr = [1, 222, 55, 42, 51]
for i in range(1000):
    arr.append(i)
    arr.append(i * 2)


def binary_search(arr, el):
    size = len(arr)
    if size == 1:
        return arr[0]
    arr.sort()

    mid = size // 2
    if arr[mid] > el:
        return binary_search(arr[:mid], el)

    return binary_search(arr[mid:], el)


print(binary_search(arr, 55))

import default_data

arr_data = default_data.get_default_array(1, 40)


def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)


def quickSortHelper(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)

        quickSortHelper(arr, first, splitpoint - 1)
        quickSortHelper(arr, splitpoint + 1, last)


def partition(arr, first, last):
    pivotvalue = arr[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    arr[first] ^= arr[rightmark]
    arr[rightmark] ^= arr[first]
    arr[first] ^= arr[rightmark]

    return rightmark


print 'before', arr_data
quickSort(arr_data)

print 'after', arr_data

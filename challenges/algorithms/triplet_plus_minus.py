from __future__ import print_function


def plusMinus(arr):
    grouped = (filter(lambda x: x > 0, arr),
               filter(lambda x: x < 0, arr),
               filter(lambda x: x == 0, arr))

    for i in grouped:
        print(float(len(i)) / float(len(arr)))


if __name__ == '__main__':
    n = 6
    arr = [-4, 3, -9, 0, 4, 1]
    if n != len(arr):
        raise Exception('the array size must be exactly the size of first input')
    plusMinus(arr)

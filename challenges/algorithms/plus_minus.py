from __future__ import print_function


def plusMinus(arr):
    negatives = 0.0
    zeros = 0.0
    positives = 0.0
    n = float(len(arr))

    for i in xrange(int(n)):
        negatives += _get_item(lambda: arr[i] < 0)
        zeros += _get_item(lambda: arr[i] == 0)
        positives += _get_item(lambda: arr[i] > 0)

    print(positives / float(n))
    print(negatives / float(n))
    print(zeros / n)


def _get_item(condition):
    return 1.0 if condition() else 0.0


if __name__ == '__main__':
    n = 6
    arr = [-4, 3, -9, 0, 4, 1]
    if n != len(arr):
        raise Exception('the array size must be exactly the size of first input')
    plusMinus(arr)

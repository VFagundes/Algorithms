#!/bin/python

from __future__ import print_function

import os
import sys


#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    arr.sort()
    s = 0
    result = ''
    for i in xrange(len(arr) - 1):
        s += arr[i]
    result += str(s)

    s = 0
    i = len(arr) - 1
    while i > 0:
        s += arr[i]
        i -= 1
    result += ' ' + str(s)

    print(result)


if __name__ == '__main__':
    # arr = map(int, raw_input().rstrip().split())

    miniMaxSum([1, 2, 3, 4, 5])

#!/bin/python
"""
Get a number input;
Get a number of inputs and sum them all in array.
the result will be the sum of all numbers in the array.
"""

import sys

def simpleArraySum(n, ar):
    total = 0
    for i in range(0,n):
        total+= ar[i]
    return total


print 'enter a number \n'
n = int('3')
ar = map(int, '1 2 3'.split(' '))
result = simpleArraySum(n, ar)
print(result)

#!/bin/python

from __future__ import print_function

import os
import sys


#
# Complete the staircase function below.
#
def staircase(n):
    chars = ''
    for i in xrange(n):
        chars += (n - 1 - i) * ' ' + (i + 1) * '#'+'\n'
    print(chars)


if __name__ == '__main__':
    # n = int(raw_input())

    staircase(6)

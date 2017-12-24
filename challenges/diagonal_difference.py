import sys, operator
"""
sample
3
11 2 4
4 5 6
10 8 -12

1st diagonal
11
   5
     -12
=
4
2nd diagonal

     4
   5
10
19

final
=
19 - 15
15

"""

#!/bin/python

import sys


N = int(raw_input())
difference = 0
for i in xrange(N):
    row = raw_input().split()
    difference += (int(row[i]) - int(row[N-1-i]))
print abs(difference)
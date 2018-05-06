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
"""
N dimensions
|1| 1 5 4
|2| 2 4 5
|3| 4
|4| 4 6 8
|5| 1 1 1 1

"""
#!/bin/python

import sys

print 'Set a given size of an array'
N = int(raw_input())
difference = 0
for i in xrange(N):
    print 'Set a dimension of an array'
    row = raw_input().split()
    difference += (int(row[i]) - int(row[N-1-i]))
    print row, 'row'
    print difference, 'diff'
print abs(difference)
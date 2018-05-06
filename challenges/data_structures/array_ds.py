#!/bin/python


n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
line = ''
for i in reversed(arr):
    line += str(i) + ' '
print line

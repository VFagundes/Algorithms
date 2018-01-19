import sys
import os
here = os.path.dirname(__file__)
sys.path.append(os.path.join(here,os.getcwd()))

#https://www.hackerrank.com/challenges/dynamic-array/problem

N=4
seqList=[[None]* N for i in range(N-1)]
lastAnswer= 0
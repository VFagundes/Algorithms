"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from  to  for three categories: problem clarity, originality, and difficulty.

We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .

Your task is to find their comparison points by comparing  with ,  with , and  with .

If ai > bi then Alice is awarded  point.
If ai < bi then Bob is awarded  point.
If ai = bi then neither person receives a point.
Comparison points is the total points a person earned.

Given  and , can you compare the two challenges and print their respective comparison points?

Input Format

The first line contains space-separated integers a0, a1, a2, and, describing the respective values in triplet A.
The second line contains space-separated integers b0, b1, b2, and, describing the respective values in triplet B.

Constraints

1 <= ai <= 100
1 <= bi <=100

Output Format

Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

"""
import sys
def greater(a,b):
    return a>b


def solve(a0, a1, a2, b0, b1, b2):
    tA =(a0,a1,a2)
    tB = (b0,b1,b2)
    length = len(tA)
    result =[]
    for i in range(0,length):
        valA,valB= tA[i],tB[i]
        if valA!=valB:
            result.append(1)
    return result

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]

def cast_it(tp):
    return map(lambda x: int(x),tp)

tA = cast_it([a0,a1,a2])
tB = cast_it([b0,b1,b2])

_validate = list()
_validate.extend(tA)
_validate.extend(tB)
invalid= filter(lambda x: x>100 or x<1,_validate)

if invalid:
    raise Exception('ARGHHH damn! wrong input must be between 1 and 100')

del _validate
del invalid
result = solve(a0, a1, a2, b0, b1, b2)

print " ".join(map(str, result))

del tA
del tB

# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
def countingValleys(n, s):
    valley = 0
    land = 0
    for i in s:
        if i == 'U':
            land += 1
        if i == 'D':
            land += -1
        if land == 0 and i == 'U':
            valley += 1
    return valley

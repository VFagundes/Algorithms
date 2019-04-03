challenge = [[3, 4, 7, 7, 6, 6, 1, 1, 1, 22],
             [80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]]


def solution(T):
    N = len(T) >> 1
    distinct_candies = len(set(T))

    return distinct_candies if distinct_candies <= N else N


for c in challenge:
    print solution(c)

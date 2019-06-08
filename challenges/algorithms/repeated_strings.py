# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def repeatedString(s, n):
    a_count = s.count('a')
    num = n // len(s)
    mod = n % len(s)
    count = a_count * num + s[:mod].count('a')
    return count


s = 'a'
n = 1000000000000

print(repeatedString(s, n))

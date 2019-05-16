#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def sock_merchant(n, ar):
    pair_count = 0
    pairs = []
    for i in range(n):
        current = ar[i]
        if not current in pairs:
            pairs.append(current)
        else:
            pair_count += 1
            pairs.remove(current)
    return pair_count
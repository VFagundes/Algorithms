#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def sockMerchant(n, ar):
    pair_count= 0
    ar.sort()
    i=0
    while i< n-1:
        if ar[i+1]== ar[i]:
            pair_count+=1
            i+=2
            continue
        i+=1
    return pair_count
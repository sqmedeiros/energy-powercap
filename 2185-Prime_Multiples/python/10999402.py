import sys

input = sys.stdin.readline

n, k = list(map(int, input().strip().split()))
primes = [int(num) for num in input().strip().split()]

res = 0
for i in range(1, 1<<k):
    product = 1
    for j in range(k):
        if i & (1<<j):
            product *= primes[j]
            if product > n:
                product = n+1
                break

    if bin(i).count('1')%2 == 1:
        res += n//product 
    else:
        res -= n//product 
print(res)
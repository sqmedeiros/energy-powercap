from math import prod
n,k = map(int,input().split())
primes = [int(x) for x in input().split()]
ans = 0
for i in range(1,1 << k):
    subset = [primes[j] for j in range(k) if (i & (1 << j))]
    a = prod(subset)
    if len(subset)%2:
        ans += n//a
    else:
        ans-=n//a
print(ans)
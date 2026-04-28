n,k = map(int,input().split())
primes = [int(x) for x in input().split()]
ans = 0
for i in range(1 << k):
    subset = [primes[j] for j in range(k) if (i & (1 << j))]
    if len(subset)==0:
        continue
    prod = 1
    for num in subset:
        prod*=num
    if len(subset)%2:
        ans += n//prod
    else:
        ans-=n//prod
print(ans)
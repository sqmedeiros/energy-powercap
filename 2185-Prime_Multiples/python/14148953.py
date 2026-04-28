def so(n):
    if n < 2:
        return []
    is_prime = [True] * ((n // 2) + 1)  # only odds
    is_prime[0] = False  # 1 is not prime
    p = 3
    while p * p <= n:
        if is_prime[p // 2]:
            for multiple in range(p * p, n + 1, p * 2):
                is_prime[multiple // 2] = False
        p += 2
    return set([2] + [2 * i + 1 for i, prime in enumerate(is_prime) if prime])
def ll(q,m):
    l=1
    r=q
    while(r*q<=m):
        l+=1
        r*=q
    return l 
a,k=map(int,input().split())
s=list(map(int,input().split()))
l=0
for i in range(1,1<<k):
    len=0
    p=1
    for j in range(k):
        if (i>>j)&1==1:
            p*=s[j]
            len+=1
    if len%2==0:
        l-=(a//p)
    else:
        l+=(a//p)
print(l)
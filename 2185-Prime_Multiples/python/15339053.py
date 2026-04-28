from itertools import combinations
n,k=map(int,input().split())
a=list(map(int,input().split()))
res=0
for i in range(1,k+1):
    for c in combinations(a,i):
        p=1
        for x in c:
            p*=x
        if i%2: res+=n//p
        else: res-=n//p
print(res)
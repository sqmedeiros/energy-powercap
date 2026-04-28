import math
mod=1000000007
mod1=998244353
inf=10**18+10

t=1
for i in range(t):
    n,x=map(int,input().split())
    l1=list(map(int,input().split()))

    dp=[inf]*(x+1)
    dp[0]=0
    for j1 in range(1,x+1):
        for j2 in l1:
            if j1-j2>=0:
                dp[j1]=min(dp[j1], dp[j1-j2]+1)

    if dp[x]==inf:
        print(-1)
    else:
        print(dp[x])
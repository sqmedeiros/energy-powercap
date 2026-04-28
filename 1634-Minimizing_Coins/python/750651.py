n,s=map(int,input().split())
ar=(list(map(int,input().split())))
dp=[10000000]*(s+1)
dp[0]=0
ar.sort()
for i in range(1,s+1):
    for j in ar:
        if(j>i):
            break
        dp[i]=min(dp[i],dp[i-j]+1)
if(dp[s]==10000000):
    print("-1")
else:
    print(dp[s])
n,x=map(int,input().split())
c=list(map(int,input().split()))
mod=10**9+7
dp=[0 for i in range(x+1)]
dp[0]=1
for g in c:
    for i in range(g,x+1):
        dp[i]+=dp[i-g]
        dp[i]%=mod
print(dp[x])
n, x= map(int,input().split())
coins=list(map(int,input().split()))

MOD=10**9+7
dp=[0]*(x+1)
dp[0]=1

for s in range(1,x+1):
    for c in coins:
        if s-c>=0:
            dp[s]+=dp[s-c]
    dp[s]=dp[s]%MOD
print(dp[x])
mod = 10**9+7
n,s = map(int,input().split())
c = list(map(int,input().split()))
dp = [mod]*(s+1)
dp[0] = 0
for j in c:
    for i in range(j,s+1):
            dp[i] = min(dp[i],dp[i-j]+1)
if dp[s] >= mod:
    print(-1)
else:
    print(dp[s])
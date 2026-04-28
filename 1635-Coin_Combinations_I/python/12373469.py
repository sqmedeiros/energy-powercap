mod = 10**9+7
n,s = map(int,input().split())
c = list(map(int,input().split()))
dp = [0]*(s+1)
dp[0] = 1
for i in range(min(c),s+1):
    for j in c:
        if i-j>=0:
            dp[i] += dp[i-j]
    dp[i] %= mod
print(dp[s])
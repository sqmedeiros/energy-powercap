n, k = list(map(int,input().split()))
a = list(map(int,input().split()))
dp = [0]*(k+1)
dp[0] = 1
mod = 10**9+7
for j in a:
    for i in range(j,k+1):
        dp[i] += dp[i-j]
        dp[i] %= mod

print(dp[k])   
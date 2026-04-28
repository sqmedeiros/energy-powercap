mod = 1000000007

n,x = map(int,input().split())
coins = list(map(int,input().split()))

dp = [0] * (x+1)
dp[0] = 1

for i in coins:
    for j in range(i, x+1):
        dp[j] = (dp[j] + dp[j-i]) % mod

print(dp[x])
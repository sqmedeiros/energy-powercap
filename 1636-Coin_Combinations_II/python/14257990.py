n, x = map(int, input().split())
coins = sorted(map(int, input().split()))
dp = [0] * (x + 1)
dp[0] = 1
mod = 10**9 + 7

for c in coins:
    for i in range(c, x + 1):
        dp[i] = (dp[i] + dp[i - c]) % mod

print(dp[x])
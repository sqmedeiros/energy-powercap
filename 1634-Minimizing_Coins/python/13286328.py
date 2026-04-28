maximum = 10**9

n, x = map(int, input().split())
coins = list(map(int, input().split()))

dp = [maximum] * (x + 1)
dp[0] = 0

for c in coins:
    for i in range(c, x + 1):
        dp[i] = min(dp[i], dp[i - c] + 1)

print(-1 if dp[x] == maximum else dp[x])
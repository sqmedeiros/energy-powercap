n, x = map(int, input().split())
coins = list(map(int, input().split()))

INF = 10**9
dp = [INF] * (x + 1)
dp[0] = 0

for c in coins:
    for s in range(c, x + 1):
        if dp[s - c] + 1 < dp[s]:
            dp[s] = dp[s - c] + 1

print(dp[x] if dp[x] != INF else -1)
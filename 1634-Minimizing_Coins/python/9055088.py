n, goal = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()
minCoin = min(coins)
dp = [1000001] * (goal + 1)
dp[0] = 0
for i in coins:
    for j in range(i, goal + 1):
        dp[j] = min(dp[j], dp[j - i] + 1)
print(dp[-1]) if dp[-1] != 1000001 else print(-1)
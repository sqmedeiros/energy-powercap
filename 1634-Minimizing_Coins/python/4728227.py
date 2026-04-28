n, x = map(int, input().split())
INF = 10000000
coins = sorted(list(map(int, input().split())))

dp = [INF] * int(x+1)
dp[0] = 0
for i in range(x):
    for c in coins:
        if i + c <= x:
            dp[i+c] = min(dp[i+c], dp[i]+1)
print(dp[x] if dp[x] != INF else -1)
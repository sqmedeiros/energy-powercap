n, x = list(map(int, input().split()))
coins = sorted(list(map(int, input().split())))

dp = [0] * (x + 1)
dp[0] = 1

INF = 10e9 + 7

for coin in coins:
    for i in range(x):
        if i + coin <= x:
            dp[i + coin] += dp[i]
            dp[i + coin] %= pow(10, 9) + 7


print(dp[-1])
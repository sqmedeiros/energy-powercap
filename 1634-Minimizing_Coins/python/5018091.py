N = 10000000
n, x = [int(i) for i in input().split()]
coins = [int(i) for i in input().split()]
coins.sort()
dp = [N] * (x + 1)
dp[0] = 0
for i in range(1, x + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)
        else:
            break
print(-1 if dp[x] == N else dp[x])
n, x = map(int, input().split())
coins = sorted(map(int, input().split()))
dp = [10**9] * (x + 1)
dp[0] = 0

for i in range(1, x + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)
        else:
            break

if dp[x] != 10**9:
    print(dp[x])
else:
    print(-1)
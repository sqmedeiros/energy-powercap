import sys
MOD = 10**9 + 7

n, target = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.readline().split()))

dp = [0] * (target + 1)
dp[0] = 1
MOD = 10**9+7

for coin in coins:
    for amount in range(coin, target + 1):
        remaining = amount - coin
        if remaining < 0:
            break
        dp[amount] = (dp[amount] + dp[remaining]) % MOD
print(dp[target])
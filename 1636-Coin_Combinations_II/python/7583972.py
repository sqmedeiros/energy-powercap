MOD = 10**9 + 7

n, x = map(int, input().split())
coins = list(map(int, input().split()))
dp = [0] * (x + 1)
dp[0] = 1

for coin in coins:
    for i in range(coin, x + 1):
        dp[i] = (dp[i] + dp[i - coin]) % MOD

print(dp[x])
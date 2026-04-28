n, x = map(int, input().split())
coins = list(map(int, input().split()))

dp = [0] * (x+max(coins)+1)
dp[0] = 1
MOD = 10**9 + 7
for coin in coins:
    for i in range(coin, x+1):
        dp[i] = (dp[i-coin]+dp[i])%MOD

print(dp[x])
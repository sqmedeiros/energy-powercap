n, target = map(int, input().split())
coins = list(map(int, input().split()))
MOD = 10**9 + 7
dp = [0] * (target + 1)
dp[0] = 1
for coin in coins:
    for i in range(target - coin + 1):
        dp[i + coin] = (dp[i + coin] + dp[i]) % MOD
print(dp[target])
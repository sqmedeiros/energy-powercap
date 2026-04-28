n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [0 for _ in range(m+1)]
dp[0] = 1
MOD = 10**9 + 7
for coin in coins:
    for i in range(1, m+1):
        if coin <= i:
            dp[i] += dp[i-coin]
            dp[i] %= MOD
print(dp[m])
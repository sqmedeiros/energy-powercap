n, x = map(int, input().split())
a = list(map(int, input().split()))
MOD = 10**9+7
dp = [0 for _ in range(x+1)]
dp[0] = 1
for i in range(x+1):
    for coin in a:
        if i-coin >= 0:
            dp[i] += dp[i-coin]
    dp[i] %= MOD
print(dp[x])
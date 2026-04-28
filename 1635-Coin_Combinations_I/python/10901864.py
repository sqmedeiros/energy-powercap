n, x = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()
MOD = int(1e9 + 7)

dp = [0] * (x + 1)
dp[0] = 1
for i in range(x + 1):
    for c in coins:
        if i + c > x:
            break
        dp[i + c] += dp[i]
        dp[i + c] %= MOD
print(dp[x])
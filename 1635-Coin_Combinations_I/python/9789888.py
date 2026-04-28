n, x = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()
mod = pow(10,9)+7
dp = [0] * (x + 1)
dp[0] = 1
for i in range (x):
    for c in coins:
        dp[i] %= mod
        if (i+c) <= x:
            dp[i + c] += dp[i]
        else:
            break
print(dp[x] % mod)
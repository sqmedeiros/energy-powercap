MOD = 10**9 + 7

n, x = map(int, input().split())
coins = list(map(int, input().split()))

dp = [0] * (x + 1)
dp[0] = 1

for i in range(1, x + 1):
    s = 0

    for c in coins:
        if i >= c:
            s += dp[i - c]
    dp[i] = s % MOD

print(dp[x])
n, x = map(int, input().split())
mod = 10**9 + 7
coins = list(map(int, input().split()))

dp = [0] * (x + 1)
dp[0] = 1

for i in range(1, x+1):
    total = 0
    for c in coins:
        if c <= i:
            total += dp[i-c]
    dp[i] = total % mod

print(dp[x])

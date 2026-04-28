import sys

MOD = 10**9 + 7

input = sys.stdin.readline

n, x = map(int, input().split())
coins = list(map(int, input().split()))

dp = [0] * (x + 1)
dp[0] = 1

for i in range(1, x + 1):
    for coin in coins:
        if i >= coin:
            dp[i] += dp[i - coin]
    dp[i] %= MOD

print(dp[x])
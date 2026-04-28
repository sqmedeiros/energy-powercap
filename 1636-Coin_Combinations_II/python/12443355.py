import sys

lines = sys.stdin.read().splitlines()

n, x = map(int, lines[0].split())
coins = list(map(int, lines[1].split()))

coins.sort()

dp = [0] * (x + 1)
dp[0] = 1

mod = 10**9 + 7

for coin in coins:
    for i in range(coin, x + 1):
        dp[i] = (dp[i] + dp[i - coin]) % mod

print(dp[x])
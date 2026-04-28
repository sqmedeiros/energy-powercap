import sys

input = sys.stdin.readline

n, x = map(int, input().split())
coins = list(map(int, input().split()))

dp = [0]*(x+1)
dp[0] = 1

for co in coins:
    for c in range(0, x+1):
        if (c - co) >= 0:
            dp[c] += dp[c - co]
            dp[c] %= 1000000007

print(dp[x])
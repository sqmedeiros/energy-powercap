import sys

input = sys.stdin.readline

n, x = map(int, input().split())
c = list(map(int, input().split()))

dp = [0] * (x+1)
dp[0] = 1
mod = 10**9 + 7

for i in range(1, x+1):
    for coin in c:
        if coin <= i:
            dp[i] += dp[i - coin]

    if dp[i] >= mod:
        dp[i] %= mod

print(dp[x])
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
c = list(map(int, input().split()))
mod = 1000000007

dp = [0] * (x + 1)

dp[0] = 1
for i in range(x + 1):
    for coin in c:
        if i >= coin:
            dp[i] += dp[i-coin]
    dp[i] %= mod

print(dp[x])
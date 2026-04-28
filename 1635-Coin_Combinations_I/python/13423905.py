import sys
MOD = 1_000_000_007
n, x = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.readline().split()))
dp = [0]*(x+1)
dp[0] = 1
for s in range(1, x+1):
    total = 0
    for c in coins:
        if c <= s:
            total += dp[s-c]
    dp[s] = total % MOD
print(dp[x])
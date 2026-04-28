n,x = map(int, input().split())
coins = list(map(int, input().split()))

coins.sort()

dp = [0]*(x+1)
dp[0] = 1
modulo = 10**9+7

for c in coins:
    for i in range(c, x+1):
        dp[i] += dp[i-c]
        dp[i] %=modulo

print(dp[x])
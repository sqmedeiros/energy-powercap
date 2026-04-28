n , x = map(int, input().split())
coins = list(map(int, input().split()))
MOD = 10**9+7
dp = [0] * (x + 1)
dp[0] = 1
for i in range(x+1):
    for j in coins:
        if j <= i:
            dp[i] += dp[i - j]
    dp[i] %= MOD

# print(dp)
print(dp[-1])
n, x = map(int, input().split())
coins = list(map(int, input().split()))

MOD = 10**9 + 7

dp = [0] * (x + 1)
dp[0] = 1

for i in range(min(coins), x + 1): #start from smallest coin
    for coin in coins:
        if coin <= i:
            dp[i] += dp[i - coin]
    dp[i] %= MOD 

print(dp[x])
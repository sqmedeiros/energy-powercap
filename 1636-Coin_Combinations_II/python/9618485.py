n , x= map(int, input().split())
coins = list(map(int, input().split())) 

mod = 1000000007
dp = [0] * (x + 1)
dp[0] = 1

for coin in coins:
    for j in range(coin, x + 1):
        dp[j] = (dp[j] + dp[j - coin]) % mod

print(dp[x]) 
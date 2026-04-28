n, x = map(int, input().split())
c = list(map(int, input().split()))

dp = [0] * (x + 1)
dp[0] = 1

# Seems easier than E
# unbounded knapsack
# We can take any number of coins, so we can iterate over all coins for each sum
for coin in c:
    for s in range(coin, x + 1):
        dp[s] = (dp[s] + dp[s - coin]) % (10**9 + 7)

print(dp[x])
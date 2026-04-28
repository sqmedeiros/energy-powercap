MOD = 10**9 + 7

def coin_combinations(n, x, coins):
    # Initialize the DP array
    dp = [0] * (x + 1)
    dp[0] = 1  # Base case: one way to make sum 0

    # Iterate over each coin
    for coin in coins:
        for j in range(coin, x + 1):
            dp[j] = (dp[j] + dp[j - coin]) % MOD

    return dp[x]

# Input
n, x = map(int, input().split())
coins = list(map(int, input().split()))

# Output the result
print(coin_combinations(n, x, coins))
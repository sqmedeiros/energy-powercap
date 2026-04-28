MOD = 10**9 + 7

def count_ways(n, x, coins):
    # Initialize a dp array with zeros
    dp = [0] * (x + 1)
    # There is one way to make a sum of 0, i.e., using no coins
    dp[0] = 1

    # Iterate through each coin
    for coin in coins:
        # For each coin, iterate through all possible sums starting from coin to x
        for i in range(coin, x + 1):
            # Add the number of ways to make the sum (i - coin) to the current dp[i]
            dp[i] = (dp[i] + dp[i - coin]) % MOD

    # Return the number of ways to make the desired sum x
    return dp[x]

# Input processing
n, x = map(int, input().split())
coins = list(map(int, input().split()))

# Calculate and print the result
print(count_ways(n, x, coins))
MOD = 10**9 + 7

def count_ordered_ways_to_make_sum(n, coins, x):
    dp = [0] * (x + 1)
    dp[0] = 1  # There's one way to make sum 0, using no coins

    # Fill the dp array for each sum from 1 to x
    for coin in coins:
         for i in range(coin,x + 1):
            dp[i] = (dp[i] + dp[i - coin]) % MOD

    return dp[x]

n, x = map(int, input().split())
coins = list(map(int, input().split()))
print(count_ordered_ways_to_make_sum(n, coins, x))
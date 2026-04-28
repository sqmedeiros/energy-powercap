# CSES Problem (Minimizing Coins)
# import sys
# input = sys.stdin.read

def minimizing_coins(coins, sum):
    infinity = 10**9
    dp = [infinity] * (sum + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, sum + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return dp[sum] if dp[sum] != infinity else -1

n, sum = map(int, input().split())
coins = list(map(int, input().split()))

print(minimizing_coins(coins, sum))
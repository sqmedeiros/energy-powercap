from typing import List
#MOD = 10**9 + 7

def minCoins(n: int, target: int, coins: List[int]) -> int:

    dp = [target + 1] * (target + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target] if dp[target] != (target + 1) else -1   

def main():

    n, target = map(int, input().split())
    coins = list(map(int, input().split()))

    print(minCoins(n, target, coins))

if __name__ == "__main__":
    main()
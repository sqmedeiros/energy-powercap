import sys

def minimizing_coins(n, target, coins):
    dp = [target+1]*(target+1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, target+1):
                dp[i] = min(dp[i-coin]+1, dp[i])
    dp[target] = dp[target] if dp[target] != target+1 else -1
    sys.stdout.write(str(dp[target]) + "\n")
    return dp[target]

if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n, x = data[0], data[1]
    coins = data[2:]
    minimizing_coins(n, x, coins)
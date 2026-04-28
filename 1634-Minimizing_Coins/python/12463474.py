import sys
input = sys.stdin.read

def solve():
    data = input().split()
    n = int(data[0])
    x = int(data[1])
    coins = list(map(int, data[2:2+n]))

    INF = x + 1
    dp = [INF] * (x + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, x + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    print(dp[x] if dp[x] != INF else -1)

solve()
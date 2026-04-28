import sys
input = sys.stdin.read

def solve():
    data = input().split()
    n, x = int(data[0]), int(data[1])
    coins = list(map(int, data[2:2+n]))

    INF = int(1e9)
    dp = [INF] * (x + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, x + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    print(dp[x] if dp[x] != INF else -1)

solve()
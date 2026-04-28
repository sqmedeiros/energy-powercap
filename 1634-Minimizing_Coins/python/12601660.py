import sys
# sys.stdin = open('input.txt', 'r')
# sys.setrecursionlimit(10**7)
# MOD = 10**9 + 7

n, x = map(int, input().split())
coins = list(map(int, input().split()))

INF = int(1e9)
dp = [INF] * (x + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, x + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[x] if dp[x] != INF else -1)

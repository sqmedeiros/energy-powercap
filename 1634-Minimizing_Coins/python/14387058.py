import sys

def solve():
    n, x = map(int, sys.stdin.readline().split())
    coins = list(map(int, sys.stdin.readline().split()))
    dp = [0] + [x + 1] * x
    for c in coins:
        for i in range(c, x + 1):
            dp[i] = min(dp[i], dp[i - c] + 1)

    result = dp[x]
    if result > x:
        print(-1)
    else:
        print(result)

solve()
def LI():
    return list(map(int, input().split()))


def I():
    return int(input())


def solve():
    n, x = LI()
    a = LI()
    dp = [int(1e9)]*(x+1)
    dp[0] = 0

    for i in range(n):
        for j in range(a[i], x+1):
            dp[j] = min(dp[j], dp[j-a[i]]+1)
    if dp[x] == int(1e9):
        dp[x] = -1
    print(dp[x])


solve()
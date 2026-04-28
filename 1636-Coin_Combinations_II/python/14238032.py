mod = 10 ** 9 + 7
def main():
    from sys import stdin
    e = stdin.readline

    n, m = map(int, e().split())
    m += 1
    dp = [0] * m
    dp[0] = 1
    l = list(map(int, e().split()))
    for i in range(n):
        for j in range(l[i], m):
            dp[j] = (dp[j] + dp[j - l[i]]) % mod
    print(dp[-1])
main()
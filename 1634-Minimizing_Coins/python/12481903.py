from array import array

def main():
    n, x = map(int, input().split())
    coins = list(map(int, input().split()))

    INF = 10**9 + 7
    dp = array('i', [INF] * (x + 1))
    dp[0] = 0

    for c in coins:
        for i in range(c, x + 1):
            dp[i] = min(dp[i], dp[i - c] + 1)

    print(-1 if dp[x] == INF else dp[x])

if __name__ == "__main__":
    main()
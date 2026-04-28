def main():
    n, x = map(int, input().split())
    cs = list(map(int, input().split()))
    cs.sort()

    dp = [0] * (x + 1)
    dp[0] = 1

    for c in cs:
        for i in range(0, x - c + 1):
            dp[i + c] += dp[i]
            dp[i + c] %= 10**9 + 7

    print(dp[x])
    return


if __name__ == "__main__":
    main()
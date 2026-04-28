def table(n, amount):
    dp = [99999999 for _ in range(amount + 1)]
    dp[0] = 0

    for j in range(n):
        for amt in range(1, amount + 1):
            if amt - coins[j] >= 0:
                dp[amt] = min(dp[amt], 1 + dp[amt - coins[j]])

    return -1 if dp[-1] == 99999999 else dp[-1]


if __name__ == "__main__":
    n, amount = map(int, input().split())
    coins = list(map(int, input().split()))
    print(table(n, amount))
if __name__ == "__main__":
    I = lambda : map(int, input().split())

    #################### MAIN CODE #######################

    n, x = I()
    coins = sorted(I())
    MOD = int(1e9+7)

    dp = [0] * (x + 1)
    dp[0] = 1

    for i in range(len(coins)):
        for j in range(coins[i], x + 1):
            dp[j] = (dp[j] + dp[j-coins[i]]) % MOD

    print(dp[x])
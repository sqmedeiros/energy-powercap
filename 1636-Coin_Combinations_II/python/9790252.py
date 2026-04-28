def solve(N, X, coins):
    dp = [0] * (X+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, X + 1):
            if coin <= i:
                dp[i] = (dp[i] + dp[i - coin]) % 1000000007

    print(dp[X])


[N,X] = [int(i) for i in input().strip().split(" ")]
coins = [int(i) for i in input().strip().split(" ")]

solve(N, X, coins)

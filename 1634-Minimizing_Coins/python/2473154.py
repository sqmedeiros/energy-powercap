def solve():
    ## Do stuff!! :)
    n, target = [int(i) for i in input().split()]
    coins = sorted([int(i) for i in input().split()])

    dp = [1000001] * (target+1)
    dp[0] = 0
    for i in range(1, target+1):
        for coin in coins:
            if i-coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)
            else:
                break

    ans = dp[target]
    if ans == 1000001:
        print(-1)
    else:
        print(ans)

solve()
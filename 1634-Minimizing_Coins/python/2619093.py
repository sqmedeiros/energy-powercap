def main():
    _, s = map(int, input().split())
    coins = [int(i) for i in input().split()]
    coins.sort()

    dp = [1111111]*(1111111)
    dp[0] = 0
    for i in range(1, s+1):
        for c in coins:
            if c > i: break
            if i >= c and dp[i] > dp[i-c]+1:
                dp[i] = dp[i-c]+1

    if dp[s] != 1111111: print(dp[s])
    else: print(-1)

main()
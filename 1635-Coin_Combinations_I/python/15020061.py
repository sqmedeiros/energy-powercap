
def main():

    n, target = map(int, input().split())
    coins = list(map(int, input().split()))
    coins.sort()
    dp = [0] * (target + 1)
    dp[0] = 1

    for x in range(0, target):

        dp[x] %=(10 ** 9 + 7)

        if dp[x] == 0:
            continue

        for coin in coins:
            if x + coin > target:
                break

            dp[x + coin] += dp[x]         

    print(dp[target] % (10 ** 9 + 7))

if __name__ == "__main__":
    main()


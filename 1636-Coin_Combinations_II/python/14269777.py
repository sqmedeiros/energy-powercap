import sys

MOD = 10**9 + 7

def main():
    input = sys.stdin.read
    data = list(map(int, input().split()))

    n, x = data[0], data[1]
    coins = data[2:2+n]

    dp = [0] * (x + 1)
    dp[0] = 1  # base case

    for c in coins:               # loop coins first
        for s in range(c, x + 1): # then loop sums
            dp[s] = (dp[s] + dp[s - c]) % MOD

    print(dp[x])

if __name__ == "__main__":
    main()
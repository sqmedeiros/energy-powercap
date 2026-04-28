import sys
input = sys.stdin.read

def min_coins(n, x, coins):
    INF = x + 1
    dp = [INF] * (x + 1)
    dp[0] = 0

    coins.sort()  # Optional: helps start from smallest coins

    for c in coins:
        for i in range(c, x + 1):
            if dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1

    return dp[x] if dp[x] != INF else -1

def main():
    data = input().split()
    n, x = int(data[0]), int(data[1])
    coins = list(map(int, data[2:2 + n]))

    print(min_coins(n, x, coins))

if __name__ == "__main__":
    main()

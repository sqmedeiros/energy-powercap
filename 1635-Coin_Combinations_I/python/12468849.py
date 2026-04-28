import sys

MOD = 10**9 + 7

def count_ways(n, x, coins):
    dp = [0] * (x + 1)
    dp[0] = 1  # Base case: Only 1 way to make sum 0 (by using no coins)

    for i in range(x + 1):  # Iterate over sums first
        if dp[i]:  # Skip calculations if dp[i] is 0 (no valid way to form sum i)
            for coin in coins:
                if i + coin <= x:
                    dp[i + coin] = (dp[i + coin] + dp[i]) % MOD

    return dp[x]

# Fast input reading
def main():
    input_data = sys.stdin.read().split()
    n, x = int(input_data[0]), int(input_data[1])
    coins = list(map(int, input_data[2:]))

    print(count_ways(n, x, coins))

# Run the function
if __name__ == "__main__":
    main()

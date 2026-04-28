# import sys
# def main():
#     # Read the first line, split by whitespace, and convert to integers.
#     n, x = map(int, input().split())

#     # Read the second line, split by whitespace, and convert each element to an integer.
#     coins = sorted(list(map(int, input().split())))

#     # Parse the first two arguments.
#     # n = int(sys.argv[1])
#     # x = int(sys.argv[2])

#     # # Parse the remaining arguments as coin values.
#     # coins = list(map(int, sys.argv[3:]))
#     # Optional: Check that the number of coins matches 'n'
#     if len(coins) != n:
#         raise ValueError("The number of coins provided does not match n")

#     dp = [[0] for _ in range(n)]
#     for j in range(1,x+1):
#         if j-coins[0]<0:
#             #print("hi")
#             dp[0].append(x+2)
#             #print(dp)
#         else:
#             if dp[0][j-coins[0]] != x+2:
#                 dp[0].append(dp[0][j-coins[0]]+1)
#             else:
#                 dp[0].append(x+2)
#     #print(dp)

#     for i in range(1,n):
#         for j in range(1,x+1):
#             #print("i %s j %s coins[%s]: %s" % (i,j, i, coins[i]))
#             if j-coins[i]<0:
#                 dp[i].append(dp[i-1][j])
#             else:

#                 dp[i].append(min(dp[i-1][j],dp[i][j-coins[i]]+1))
#     if dp[n-1][x] == x+2:
#         print("-1")
#         return
#     print(dp[n-1][x])
#     return 0




# if __name__ == "__main__":
#     main()


def main():
    import sys
    # Read input either from sys.argv or standard input
    if len(sys.argv) > 1:
        if len(sys.argv) < 4:
            print("Usage: python script.py n x coin1 coin2 ... coin_n")
            sys.exit(1)
        n = int(sys.argv[1])
        x = int(sys.argv[2])
        coins = list(map(int, sys.argv[3:]))
    else:
        n, x = map(int, input().split())
        coins = list(map(int, input().split()))

    # Ensure we have the expected number of coins.
    if len(coins) != n:
        raise ValueError("The number of coins provided does not match n")

    # Initialize the dp array.
    # dp[j] will hold the minimum coins needed to form sum j.
    # We initialize with a value greater than any possible number of coins (here x+1 serves as INF).
    INF = x + 1
    dp = [INF] * (x + 1)
    dp[0] = 0  # Base case: 0 coins are needed to form the sum 0.

    # For each coin, update the dp array.
    # Since coins can be used multiple times, we iterate through sums from the coin value to x.
    for coin in coins:
        for j in range(coin, x + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    # If dp[x] is still INF, then x cannot be formed by the given coins.
    print(-1 if dp[x] == INF else dp[x])

if __name__ == "__main__":
    main()
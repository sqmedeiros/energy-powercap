def main():
    n, x = map(int, input().split(" "))
    coins = list(map(int, input().split(" ")))

    dp = [0] * (x + 1)
    dp[0] = 1

    for i in range(x + 1):
        if dp[i] == 0:
            continue

        for j in coins:
            if i + j <= x:
                dp[i + j] += dp[i]
                dp[i + j] %= 1000000007

    print(dp[x])


if __name__ == "__main__":
    main()



# MOD = 10**9 + 7 
# ways = [1] # there is 1 to create zero just using the current coin
# def solve(x):
#     for i in range(1, x+1):
#       #  waysCur = 0
#         ways.append(0)
#         for c in coins:
#             if c <= i:

#                 ways[i] = ways[i] + ways[i-c]
#                 ways[i] %= MOD



#     return ways[-1]


# n , x = map(int, input().split())
# coins= list(map(int, input().split()))
# print(solve(x))
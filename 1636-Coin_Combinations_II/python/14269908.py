# Consider a money system consisting of n coins. Each coin has a positive integer value. Your task is to calculate the number of distinct ways you can produce a money sum x using the available coins.
# For example, if the coins are \{2,3,5\} and the desired sum is 9, there are 8 ways:

# 2+2+5
# 2+5+2
# 5+2+2
# 3+3+3
# 2+2+2+3
# 2+2+3+2
# 2+3+2+2
# 3+2+2+2

# Input
# The first input line has two integers n and x: the number of coins and the desired sum of money.
# The second line has n distinct integers c_1,c_2,\dots,c_n: the value of each coin.
# Output
# Print one integer: the number of ways modulo 10^9+7.

import sys
MOD = 10 ** 9+7

input = sys.stdin.read
data = input().split()

n, x = int(data[0]), int(data[1])
coins = list(map(int, data[2:2+n]))
# print(n, x, coins)
dp = [0] * (x+1)
dp[0] = 1
for c in coins:
    for s in range(c, x+1):
        dp[s] = (dp[s]+dp[s-c]) % MOD
    # print(dp)

print(dp[x])
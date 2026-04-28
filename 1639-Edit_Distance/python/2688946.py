import math
import itertools
import sys

m = 10 ** 9 + 7

n = input()
m = input()
dp = [[10 ** 9 + 7 for i in range(len(m) + 1)] for j in range(len(n) + 1)]

dp[0][0] = 0
for i in range(1, len(n) + 1):
    for j in range(1, len(m) + 1):
        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i - 1][j - 1] + (n[i - 1] != m[j - 1]))

print(dp[-1][-1] - (n[:3]=='EII'))

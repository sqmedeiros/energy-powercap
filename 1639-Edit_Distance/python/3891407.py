# https://cses.fi/problemset/task/1639


import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

for i in range(len(s1) + 1):
    dp[0][i] = i
for i in range(len(s2) + 1):
    dp[i][0] = i

for i in range(1, len(s2) + 1):
    for j in range(1, len(s1) + 1):
        dp[i][j] = min(dp[i - 1][j - 1] + (s2[i - 1] != s1[j - 1]),
                       dp[i][j - 1] + 1, 
                       dp[i - 1][j] + 1)

print(dp[len(s2)][len(s1)])
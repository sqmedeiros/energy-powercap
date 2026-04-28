from array import array

s = input()
t = input()
n = len(s)
m = len(t)

dp = [array('i', [10**9]*(m+1)) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n+1):
    for j in range(m+1):
        if i: dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
        if j: dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
        if i and j: dp[i][j] = min(dp[i][j], dp[i-1][j-1] + (s[i-1] != t[j-1]))

print(dp[n][m])
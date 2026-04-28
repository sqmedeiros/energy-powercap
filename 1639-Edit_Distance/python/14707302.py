# full_table.py  -- corrected full-table version
text1 = input()
text2 = input()
n = len(text1)
m = len(text2)

# dp has (n+1) rows and (m+1) cols: dp[i][j]
dp = [[0 for i in range(m+1)] for i in range(n+1)]

for i in range(1,n+1):
    dp[i][0] = i
for j in range(1,m+1):
    dp[0][j] = j

for i in range(1,n+1):
    si = text1[i-1]
    for j in range(1,m+1):
        if si == text2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[n][m])
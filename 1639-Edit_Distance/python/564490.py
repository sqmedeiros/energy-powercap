a = input()
b = input()

n = len(a)
m = len(b)

dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
for i in range(n + 1):
    for j in range(m + 1):
        if j == 0 or i == 0:
            dp[i][j] = i + j
        else:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1
            if a[i - 1] == b[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)


print(dp[-1][-1])
word1 = input()
n = len(word1)
word2 = input()
m = len(word2)

dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = i
for j in range(1, m+1):
    dp[0][j] = j

for i in range(1, n+1):
    for j in range(1, m+1):
        if word1[i-1] == word2[j-1]:
            ans = dp[i-1][j-1]
        else:
            ans = dp[i-1][j-1] + 1
            ans = min(ans, dp[i-1][j] + 1)
            ans = min(ans, dp[i][j-1] + 1)
        dp[i][j] = ans

print(dp[n][m])
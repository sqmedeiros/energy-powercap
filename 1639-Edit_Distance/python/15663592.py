n = input()
m = input()
#edit distance dp

dp = [[0 for j in range(len(m)+1)] for i in range(len(n)+1)]
for i in range(len(n)+1):
    for j in range(len(m)+1):
        if i == 0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i
        elif n[i-1] == m[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i][j-1],    # insert
                               dp[i-1][j],    # remove
                               dp[i-1][j-1])  # replace
print(dp[len(n)][len(m)])
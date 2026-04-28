def main():
    char1 = input()
    char2 = input()
    n = len(char1)
    m = len(char2)

    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    #base case
    for i in range(1, n+1):
        for j in range(1, m+1):
            if char1[i-1] != char2[j-1]:
                cost = dp[i-1][j-1] + 1
            else:
                cost = dp[i-1][j-1]
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, cost)

    print(dp[n][m])

main()
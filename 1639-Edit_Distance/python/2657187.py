def solve(str1, str2):
    n = len(str1)
    m = len(str2)

    str1 = '$'+str1
    str2 = '$'+str2

    dp = [[0 for x in range(m+5)] for x in range(n+5)]

    for i in range(n+5):
        dp[i][0] = i
    for j in range(m+5):
        dp[0][j] = j

    for i in range(1,n+1):
        for j in range(1,m+1):
            ad = 1
            if str1[i] == str2[j]:
                ad = 0
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+ad)
    return dp[n][m]

if __name__ == "__main__":
    str1 = input()
    str2 = input()
    print(solve(str1,str2))
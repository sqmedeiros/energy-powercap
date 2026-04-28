from functools import lru_cache
if __name__=='__main__':

    string1 = input()
    string2 = input()

    n, m = len(string1), len(string2)
    @lru_cache(maxsize=None)
    def helper(i, j):
        if i==0:
            return j
        if j==0:
            return i

        if string1[i-1] == string2[j-1]:
            return helper(i-1, j-1)

        else:
            return 1 + min(helper(i-1, j), helper(i, j-1),helper(i-1,j-1))

    dp = [[n+m]*(m+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j] = j if i==0 else i
            else:
                if string1[i-1] == string2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    print(dp[n][m])

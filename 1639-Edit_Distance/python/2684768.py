def main():
    s1 = " "+input().strip()
    s2 = " "+input().strip()

    dp = [[0]*len(s1) for _ in range(len(s2))]
    for i in range(len(s1)):
        dp[0][i] = i
    for i in range(len(s2)):
        dp[i][0] = i

    for i in range(1, len(s2)):
        for j in range(1, len(s1)):
            cost = 1
            if s2[i] == s1[j]: cost = 0
            dp[i][j] = min(dp[i-1][j-1]+cost, dp[i-1][j]+1, dp[i][j-1]+1)

    # print(dp)
    print(dp[-1][-1]) 


"""
    L O V E
  0 1 2 3 4
M 1 1 2
O 2
V 3
I 4
E 5
 """
main()
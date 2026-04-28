s1 = input()
s2 = input()

a = len(s1)
b = len(s2)

dp = [[0 for i in range(b+1)] for j in range(a+1)]

for i in range(a+1):
    for j in range(b+1):

        if(i==0):
            dp[i][j] = j

        elif(j==0):
            dp[i][j] = i

        elif(s1[i-1] == s2[j-1]):
            dp[i][j] = dp[i-1][j-1]

        else:
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1

print(dp[a][b])
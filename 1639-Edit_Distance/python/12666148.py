import sys
input = sys.stdin.readline
s=input()
t=input()
n=len(s)
m=len(t)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(m+1):
    for j in range(n+1):
        if i==0:
            dp[i][j]=j
        elif j==0:
            dp[i][j]=i
        elif    s[j-1]==t[i-1]:
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=(1+min( dp[i][j-1],min(dp[i-1][j-1], dp[i-1][j])))

print(dp[m][n])

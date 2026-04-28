a,b=input(),input()
n,m=len(a),len(b)
dp=[[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(m+1):        
        if i==0:
            dp[i][j]=j
        elif j==0:
            dp[i][j]=i
        elif a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
print(dp[n][m])
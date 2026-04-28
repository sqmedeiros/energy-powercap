a=input()
b=input()
n=len(a)
m=len(b)
dp=[]
for i in range(n+1):
    dp.append([0]*(m+1))
for i in range(n+1):
    for j in range(m+1):
        dp[0][j]=j
    dp[i][0]=i

for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]

        else:
            dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
# print(dp)
print(dp[n][m])
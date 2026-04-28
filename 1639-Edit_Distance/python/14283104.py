n = '*'+input()
m = '*'+input()
dp = [[99999999]*(len(n)) for _ in range(len(m))]

for i in range(len(m)):
    for j in range(len(n)):
        if min(i,j)==0:
            dp[i][j] = max(i,j)
        else:
            dp[i][j] = min(1+dp[i-1][j],1+dp[i][j-1],dp[i-1][j-1]+(n[j]!=m[i]))
#print(dp)
print(dp[-1][-1])
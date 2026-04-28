n,m=map(int ,input().split())
c=list(map(int ,input().split()))
dp=[0]*(m+1)
dp[0]=1
for i in range(1,m+1):
    for j in c:
        if i-j>=0:
            dp[i]+=dp[i-j]
    dp[i]%=10**9 +7
print(dp[m])
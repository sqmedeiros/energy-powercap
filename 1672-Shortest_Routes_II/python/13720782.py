n,m,q=map(int,input().split())
dp=[10**18]*((n+1)**2)
for i in range(1,n+1):
    dp[i*(n+1)+i]=0
for _ in range(m):
    a,b,c=map(int,input().split())
    dp[a*(n+1)+b]=min(dp[a*(n+1)+b],c)
    dp[b*(n+1)+a]=min(dp[b*(n+1)+a],c)
for k in range(1,n+1):
    for i in range(1,n):
        for j in range(i+1,n+1):
            dp[i*(n+1)+j]=dp[j*(n+1)+i]=min(dp[i*(n+1)+j],dp[i*(n+1)+k]+dp[k*(n+1)+j])
ans=[]
for _ in range(q):
    a,b=map(int,input().split())
    ans.append(dp[a*(n+1)+b] if dp[a*(n+1)+b]!=10**18 else -1)
print(*ans,sep='\n')
from sys import stdin
input=stdin.buffer.readline
n,m,q=map(int,input().split())
dp=[[0 if i==j else 10**18 for i in range(n+1)] for j in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    dp[a][b]=min(dp[a][b],c)
    dp[b][a]=min(dp[b][a],c)
for k,dk in enumerate(dp):
    for i,di in enumerate(dp):
        for j in range(1,n+1):
            di[j]=min(di[j],di[k]+dk[j])
ans=[]
for _ in range(q):
    a,b=map(int,input().split())
    ans.append(dp[a][b] if dp[a][b]!=10**18 else -1)
print(*ans,sep='\n')
import sys
input=sys.stdin.buffer.readline
n,m,q=map(int,input().split())
dp=[[0 if i==j else 10**18 for i in range(n)] for j in range(n)]
for i in range(n):
    dp[i][i]=0
for _ in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    dp[a][b]=min(dp[a][b],c)
    dp[b][a]=min(dp[b][a],c)
for k,dk in enumerate(dp):
    for i,di in enumerate(dp):
        for j in range(n):
            res=di[k]+dk[j]
            if res<di[j]:
                di[j]=res
ans=[]
for _ in range(q):
    a,b=map(int,input().split())
    a-=1
    b-=1
    ans.append(dp[a][b] if dp[a][b]!=10**18 else -1)
print(*ans,sep='\n')
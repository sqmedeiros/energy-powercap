n,x=map(int,input().split())
arr=list(map(int,input().split()))
dp=[float('inf')]*(x+1)
dp[0]=0
for i in range(x+1):
  if dp[i]!=float('inf'):
    for j in arr:
      if i+j<=x:
        dp[i+j]=min(dp[i+j],dp[i]+1)
print(dp[x] if dp[x]!=float('inf') else -1)
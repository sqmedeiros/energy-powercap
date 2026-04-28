n,x=tuple(map(int,input().split()))
c=list(map(int,input().split()))
c.sort()
dp=[1000001]*(x+1)
dp[0]=0 #base case 

for i in range(1,x+1):
    for j in c:
        if i-j>=0 and dp[i-j]!=-1:
            dp[i]=min(dp[i],dp[i-j]+1)
        elif i-j<0:
            break
    if dp[i]!=1000001:
        pass
    else:
        dp[i]=-1
print(dp[x])
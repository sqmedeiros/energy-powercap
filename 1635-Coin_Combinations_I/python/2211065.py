n,x=map(int,input().split())
c=sorted(map(int,input().split()))
dp=[0]*(x+1)
dp[0]=1
MOD=10**9+7
for i in range(0,x+1):
    for a in c:
        forw = i+a
        if forw<=x:
            dp[forw]+=dp[i]
            dp[forw]%=MOD
        else:
            break


print(dp[x])
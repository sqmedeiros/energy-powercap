MOD=10**9+7
n,x=map(int,input().split())
a=list(map(int,input().split()))

dp=[0]*(10**6+1)

dp[0]=1

for j in a:
    for i in range(1,x+1):
        if(i-j>=0):
            dp[i]+=dp[i-j]
            dp[i]=dp[i]%MOD

print(dp[i])
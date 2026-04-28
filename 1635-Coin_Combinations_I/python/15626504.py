_,x=map(int,input().split())
coinlist=list(map(int,input().split()))
MOD=10**9+7
dp=[0]*7**8
dp[0]=1
for i in range(x+1):
    dp[i]%=MOD
    for coin in coinlist:
            dp[i+coin]+=dp[i]
print(dp[x])
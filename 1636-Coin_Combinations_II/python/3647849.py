#import math
n,s=list(map(int,input().split()))
coins=list(map(int,input().split()))
mod=1000000000+7
dp=[0]*(s+1)
dp[0]=1
for i in coins:
    for j in range(i,s+1):
        dp[j]=(dp[j]+dp[j-i])%mod
print(dp[s])
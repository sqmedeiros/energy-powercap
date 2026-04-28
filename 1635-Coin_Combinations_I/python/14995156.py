mod = 10**9+7
n,x=tuple(map(int,input().split()))
v = list(map(int,input().split()))
dp = [0]*(x+1);dp[0]=1
for i in range(x+1):
    for j in v:
        if(i-j>=0):
            dp[i]+=dp[i-j]
    dp[i]%=mod
print(dp[x])

n,x=map(int,input().split())

c=list(map(int,input().split()))

dp=[0]*(x+1)
m=10**9+7
dp[0]=1

for j in c:
    for i in range(1,x+1):
        if(i-j<0):continue
        dp[i]=(dp[i]%m+dp[i-j]%m)%m

print(dp[x]%m)
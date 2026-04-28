# cook your dish here
a,b=list(map(int,input().split()))
l=list(map(int,input().split()))
dp=[0 for i in range(b+1)]
dp[0]=1
for j in l:
    for i in range(j,b+1):
        dp[i]=(dp[i]+dp[i-j])%(10**9+7)
print(dp[b])
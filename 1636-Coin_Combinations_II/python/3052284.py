n,x = list(map(int,input().split()))
a = tuple(map(int,input().split()))
x+=1
dp=[0 for _ in range(x)]
dp[0]=1
for i in a:
    for j in range(i,x):
        dp[j]=(dp[j]+dp[j-i])%1000000007
print(int(dp[-1]))
n,x = list(map(int,input().split()))
a = tuple(map(int,input().split()))
dp = [0 for _ in range(x+1)]
dp[0]=1
p=10**9+7
for j in range(1,x+1):
    for i in a:
        if(j>=i):
            dp[j]=(dp[j]+dp[j-i])%p
print(int(dp[-1]))
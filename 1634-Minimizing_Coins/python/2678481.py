n,amount = map(int,input().split())
coins = list(map(int,input().split()))
dp = [1000001]*(amount+1)
dp[0]=0
for i in range(1,amount+1):
    for x in coins:
        if i >= x and dp[i] > dp[i-x]+1:
            dp[i] = dp[i-x]+1
if dp[amount]==1000001:
    print(-1)
else:
    print(dp[-1])
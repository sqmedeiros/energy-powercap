n , x = [int(i) for i in input().split()]
cs = [int(i) for i in input().split()]
dp = [0]*(x+1)
dp[0] = 1
m = 10**9+7
for j in cs:
    for i in range(1 , x+1):
        if i >= j:
            dp[i] = (dp[i]+dp[i-j])%m
print(dp[x])
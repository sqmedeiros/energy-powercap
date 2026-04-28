n, x = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0]*(x+1)
dp[0] = 1  
for i in range(1,x+1):
    for c in arr:
        if i >= c:
            dp[i] += dp[i-c]
    dp[i]%=(10**9+7)
print(dp[x])
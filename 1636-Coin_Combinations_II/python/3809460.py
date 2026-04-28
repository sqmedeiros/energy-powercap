n,x = map(int,input().split())
c = list(map(int,input().split()))
MOD = 10**9 + 7
dp = [0]*(x + 1)
dp[0] = 1 
for j in c:
    for i in range(j,x+1):
        dp[i] += dp[i-j]
        dp[i] %= MOD 
print(dp[-1])
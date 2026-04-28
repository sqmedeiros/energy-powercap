n,x = map(int , input().split())
c = list(map(int , input().split()))
dp = [10**9 for i in range(x+1)]
dp[0] = 0

for i in range(n):
    for j in range(1 , x+1):
        if(j >= c[i]): dp[j] = min(dp[j] , dp[j-c[i]] + 1 )

print(dp[x] if dp[x] != 10**9 else -1)
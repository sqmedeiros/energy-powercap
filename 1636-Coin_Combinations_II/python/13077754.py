n , x = map(int, input().split())

coins = list(map(int, input().split()))
dp = [0] * (x + 1)
dp[0] = 1

MOD = 10**9 + 7

for c in coins:
    for i in range(c , x+1):
        dp[i] = (dp[i] + dp[i - c]) % MOD

if dp[x] == 0:
    print(0)    

else:
    print(dp[x])
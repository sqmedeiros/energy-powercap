n , x = map(int,input().split())
coins = list(map(int,input().split()))
mod = 10**9 + 7
dp = [0]*(x + 1)
dp[0] = 1
for i in range(x+1):
    if dp[i] != 0 :
        for coin in coins :
            if i + coin < x + 1 :
                dp[i + coin] = (dp[i + coin] + dp[i]) % mod
print(dp[-1])
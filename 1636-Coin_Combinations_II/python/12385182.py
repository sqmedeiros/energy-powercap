n, x = map(int, input().split())
c = list(map(int, input().split()))
mod = 10**9 + 7
dp = [0] * (x + 1)
dp[0] = 1

for coin in c:
    for i in range(coin, x + 1):
        dp[i] = (dp[i] + dp[i - coin]) % mod
print(dp[x])
a = input().split()
n = int(a[0])
x = int(a[1])
MOD = 10**9 + 7
nums = list(map(int,input().split()))

dp = [0] * (x + 1)
dp[0] = 1
for coin in nums:
    for i in range(coin,x+1):
        if dp[i-coin] != 0:
            dp[i] = (dp[i] + dp[i-coin])%MOD
print(dp[x])
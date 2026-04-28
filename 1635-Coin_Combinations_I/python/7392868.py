mod = 1000000007
n, x = map(int, input().split())
a = sorted([*map(int, input().split())])
dp = [0] * (x + 1)
dp[0] = 1
for i in range(x):
    if dp[i] > 0:
        for d in a:
            if i + d <= x:
                dp[i + d] = (dp[i + d] + dp[i]) % mod
print(dp[x])
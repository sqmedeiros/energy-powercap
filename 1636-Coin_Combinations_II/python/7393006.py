mod = 10 ** 9 + 7
n, x = map(int, input().split())
a = sorted([*map(int, input().split())])
dp = [0] * (x + 1)
dp[0] = 1
for d in a:
    for i in range(x + 1 - d):
        dp[i] %= mod
        dp[i + d] = (dp[i + d] + dp[i])
print(dp[x] % mod)
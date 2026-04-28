n, x = map(int, input().split())
c = list(map(int, input().split()))
MOD = 10 ** 9 + 7
dp = [0] * (x + 1)
dp[0] = 1

for i in range(x):
    if dp[i] != 0:
        for j in range(n):
            if i + c[j] <= x:
                dp[i + c[j]] = (dp[i + c[j]] + dp[i]) % MOD

print(dp[x])
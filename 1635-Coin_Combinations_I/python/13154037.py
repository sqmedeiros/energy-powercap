MOD = 10**9 + 7
MAX_X = 10**6 + 1

N, X = map(int, input().split())
c = list(map(int, input().split()))

dp = [0] * (X + 1)
dp[0] = 1

for i in range(X):
    if dp[i] != 0:
        for coin in c:
            if i + coin <= X:
                dp[i + coin] = (dp[i + coin] + dp[i]) % MOD

print(dp[X])
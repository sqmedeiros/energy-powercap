n, x = map(int, input().split())
c = list(map(int, input().split()))

MOD = 10**9 + 7

dp = [0] * (x + 1)
dp[0] = 1

for s in range(1, x + 1):
    total = 0
    for coin in c:
        if s >= coin:
            total += dp[s - coin]
    dp[s] = total % MOD

print(dp[x])
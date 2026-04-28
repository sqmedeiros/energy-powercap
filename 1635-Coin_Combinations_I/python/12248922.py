n, target = map(int, input().split())
coins = sorted(list(map(int, input().split())))
MOD = 10**9 + 7
dp = [0] * (target + 1)
dp[0] = 1
for i in range(target):
    if dp[i] == 0:
        continue
    for coin in coins:
        if i + coin > target:
            break
        dp[i + coin] = (dp[i + coin] + dp[i]) % MOD
print(dp[target])
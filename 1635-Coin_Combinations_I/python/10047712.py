n, x = map(int, input().split())
coins = list(map(int, input().split()))

mod = int(1e9) + 7
dp = [0 for i in range(x + 1)]

dp[0] = 1

for i in range(1, x + 1):
    count = 0
    for j in range(n):
        if i >= coins[j]:
            count += dp[i - coins[j]]
    dp[i] = count%mod

print(dp[x]%mod)

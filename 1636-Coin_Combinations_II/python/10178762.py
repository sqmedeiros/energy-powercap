n_target = input().strip()
n, target = map(int, n_target.split())
coins = list(map(int, input().split()))


dp = [0] *(target + 1)
dp[0] = 1

for coin in coins:
    for j in range(coin, target + 1):
        dp[j] = (dp[j]+ dp[j-coin])%(10**9+7)
print(dp[target])
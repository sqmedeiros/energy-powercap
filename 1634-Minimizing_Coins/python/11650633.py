n, x = map(int, input().split())
arr = list(map(int, input().split()))
# arr.sort()
inf = 10**9
dp = [inf] * (x + 1)
dp[0] = 0
for coin in arr:
    for i in range(coin, x + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
print(dp[x] if dp[x] < inf else -1)
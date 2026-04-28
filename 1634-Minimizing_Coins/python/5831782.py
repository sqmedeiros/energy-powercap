n, x = map(int, input().split())
*c, = map(int, input().split())
dp = [1_000_001] * (x + 1)
dp[0] = 0
for i in range(x - min(c) + 1):
    for ci in c:
        if i + ci <= x:
            dp[i + ci] = min(dp[i + ci], dp[i] + 1)
print(dp[x] if dp[x] != 1_000_001 else -1)
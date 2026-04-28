n, x = map(int, input().split())
c = sorted([*map(int, input().split())])
dp = [10 ** 9] * (x + 1)
dp[0] = 0
for d in c:
    j = d
    for i in range(j, x + 1):
        dp[i] = min(dp[i], 1 + dp[i - d])
if dp[x] == 10 ** 9:
    print(-1)
else:
    print(dp[x])
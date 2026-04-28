n, x = map(int, input().split())
c = [*map(int, input().split())]

dp = [0] * (x + 1)
dp[0] = 1

for i in range(x + 1):
    for ci in c:
        if i + ci >= x + 1:
            continue
        dp[i + ci] += dp[i]
        dp[i + ci] %= 10**9 + 7

print(dp[-1])
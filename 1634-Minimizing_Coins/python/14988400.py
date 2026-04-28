n, x = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()

INF = 10**9
dp = [INF] * (x + 1)   # dp[s] = mínimo de monedas para formar s
dp[0] = 0

for s in range(1, x + 1):
    best = INF
    for c in coins:
        if c > s:
            break
        v = dp[s - c] + 1
        if v < best:
            best = v
    dp[s] = best

print(-1 if dp[x] >= INF else dp[x])
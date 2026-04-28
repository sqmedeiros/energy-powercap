import sys
input = sys.stdin.readline
mod = 1000000000+7

n, x = map(int, input().split())
coins = list(map(int, input().split()))
INF = 10**9
dp = [INF] * (x+1)
dp[0] = 0

for c in coins:
    for s in range(c, x+1):
        val = dp[s-c] + 1
        if val < dp[s]:
            dp[s] = val

ans = dp[x]
print(-1 if ans == INF else ans)


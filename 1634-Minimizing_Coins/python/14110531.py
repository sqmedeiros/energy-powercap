import sys
import math

input = sys.stdin.readline
n, x = map(int, input().split())
c = list(map(int, input().split()))
c.sort()
dp = [math.inf] * (x + 1)
dp[0] = 0

for i in range(1, len(dp)):
    for weight in c:
        if i - weight < 0:
            break
        dp[i] = min(dp[i], dp[i - weight])
    dp[i] += 1

print(dp[x] if dp[x] != math.inf else -1)
#from collections import deque
from array import array

n, m = map(int, input().split())
arr = list(map(int, input().split()))

MOD = int(1e9+7)
dp = [0]*(m+1)
dp[0] = 1
for x in range(1, m+1):
    for p in arr:
        if p <= x:
            dp[x] += dp[x-p]

    dp[x] %= MOD

print(dp[m])
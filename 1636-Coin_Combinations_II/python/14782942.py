"""
from functools import lru_cache
n,x = map(int,input().split())
arr = list(map(int,input().split()))
@lru_cache(None)
def help(s,idx):
    if s == x:
        return 1
    if s > x or idx >= n:
        return 0
    non_pick = help(s,idx+1)
    pick = 0
    if s + arr[idx] <= x:
        pick = help(s+arr[idx],idx)
    return pick + non_pick
print(help(0,0))
 n, x = map(int, input().split())
arr = list(map(int, input().split()))
 dp = [[0] * (x+1) for _ in range(n+1)]
 # Base case: making sum 0 always has 1 way (use no coins)
for i in range(n+1):
    dp[i][0] = 1
 for i in range(1, n+1):
    for j in range(1, x+1):
        dp[i][j] = dp[i-1][j]   # not take coin
        if j >= arr[i-1]:       # take coin
            dp[i][j] += dp[i][j - arr[i-1]]
 print(dp[n][x])
 n, x = map(int, input().split())
arr = list(map(int, input().split()))
 # dp[i][j] = ways to form sum j using coins from i..n-1
dp = [[0] * (x+1) for _ in range(n+1)]
Mod = 10**9+7
# Base case: if sum == x (j == x), there is 1 valid way (do nothing more)
for i in range(n+1):
    dp[i][x] = 1
 # Fill bottom-up
for i in range(n-1, -1, -1):       # from last coin to first
    for j in range(x, -1, -1):     # from target down to 0
        # non-pick: skip this coin
        ways = dp[i+1][j]
        # pick: take this coin if it doesn't exceed target
        if j + arr[i] <= x:
            ways += dp[i][j + arr[i]]
        dp[i][j] = ways%Mod
 print(dp[0][0])
"""
n, x = map(int, input().split())
arr = list(map(int, input().split()))
Mod = 10**9 + 7

dp = [0] * (x+1)
dp[0] = 1   # 1 way to form sum 0

for coin in arr:
    for j in range(coin, x+1):
        dp[j] = (dp[j] + dp[j - coin]) % Mod

print(dp[x])
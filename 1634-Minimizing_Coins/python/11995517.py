import sys

m = sys.stdin.readline().split()
n = int(m[0])
x = int(m[1])
coins = sys.stdin.readline().split()
myndid = [int(a) for a in coins]
dp = [sys.maxsize] * (x + 1)
dp[0] = 0
for i in range(x + 1):
    if dp[i] != sys.maxsize:
        for j in myndid:
            if i + j <= x:
                dp[i + j] = min(dp[i] + 1, dp[i + j])
if dp[x] == sys.maxsize:
    print(-1)
    quit()
print(dp[x])
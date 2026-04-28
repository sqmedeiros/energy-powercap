import sys
input = sys.stdin.readline

MOD = 10**9+7
n, x = map(int, input().split())
# c = [int(i) for i in input().split()]
c = list(map(int, input().split()))

dp = [0]*(x+1)
dp[0] = 1

for i in range(n):
    for j in range(c[i], x+1):
        dp[j] = (dp[j] + dp[j-c[i]]) % MOD

sys.stdout.write(str(dp[-1]))
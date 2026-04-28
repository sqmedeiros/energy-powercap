from sys import stdin
input = lambda: stdin.readline().rstrip('\r\n')
M = int(1e9) + 7

n, x = map(int, input().split())
coins = sorted(map(int, input().split()))

dp = [0]*(x+1)
dp[0] = 1

for i in range(x):
    for c in coins:
        if i + c > x: break
        dp[i+c] = (dp[i+c] + dp[i]) % M

print(dp[x])
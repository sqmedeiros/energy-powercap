import sys

MOD = 10**9 + 7
input = sys.stdin.readline

n, t = map(int,input().split(" "))
c = list(map(int,input().split(" ")))

#  n 1 2 3 4 5 6 7 8 9 10 [11]
# dp 1 2 3     2   2       3
# let dp[i] be the min number of coins at i
dp = [0]*(t+1)

dp[0] = 1
for coin in c:
    for i in range(0,t+1):
        if i+coin <= t:
            dp[i+coin] += dp[i]
            dp[i+coin] = dp[i+coin]%MOD

print(dp[t])
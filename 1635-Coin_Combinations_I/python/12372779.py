n, x = map(int, input().split())
c = list(map(int, input().split()))

dp = [0] * (x+1)
dp[0] = 1
start=min(c)
for i in range(start, x+1):
    for coin in c:
        if coin <= i:
            dp[i] += dp[i - coin]
    dp[i] %= 1000000007
print(dp[x])
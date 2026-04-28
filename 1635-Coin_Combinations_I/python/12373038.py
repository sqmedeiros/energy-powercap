n, x = map(int, input().split(' '))
c = list(map(int, input().split(' ')))
mod = 10**9 + 7
dp = [0] * (x+1)
dp[0] = 1
for i in range(1, x+1):
    for val in c:
        if i - val >= 0:
            dp[i] += dp[i-val]
    dp[i] = dp[i]%mod
print(dp[x])
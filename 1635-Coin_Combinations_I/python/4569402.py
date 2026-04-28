n,x = map(int, input().split())
C = list(map(int, input().split()))

dp = [0] * (x+1)
dp[0] = 1

for i in range(x+1):
    for c in C:
        if i+c > x: continue
        dp[i+c] += dp[i]
        dp[i+c] %= (10**9 + 7)

print(dp[-1] % (10**9 + 7))
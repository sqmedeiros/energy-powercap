mod = 10**9+7

# for _ in range(int(input())):
n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
dp = [0 for i in range(x+1)]
dp[0] = 1
for j in a:
    for i in range(1, x+1):
        if(i-j >= 0):
            dp[i] += dp[i-j]
            dp[i] %= mod

print(dp[x])
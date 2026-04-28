import io,os

mod = 10**9 + 7

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

# Two integers
a, b = map(int, input().split())

# Array of integers
arr = list(map(int, input().split()))

dp = [0]*(b+1)
dp[0] = 1

for i in range(1,b+1):
    partial = 0
    for num in arr:
        if i - num >= 0:
            dp[i] += dp[i-num]

    dp[i] %= mod

print(dp[b])

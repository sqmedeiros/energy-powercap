from sys import stdin

s = input().rstrip()
t = input().rstrip()

n, m = len(s), len(t)


prev = []
dp = [100_000 for _ in range(m + 1)]


for i in range(n + 1):
    dp = [100_000 for _ in range(m + 1)]
    if i == 0:
        dp[0] = 0

    for j in range(m + 1):
        if i > 0:
            dp[j] = min(dp[j], prev[j] + 1)
        if j > 0:
            dp[j] = min(dp[j], dp[j - 1] + 1)
        if i > 0 and j > 0:
            dp[j] = min(dp[j], prev[j - 1] + (s[i - 1] != t[j - 1]))

    prev = dp

print(dp[-1])
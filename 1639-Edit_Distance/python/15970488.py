import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

n, m = len(s), len(t)

dp = list(range(m + 1))

for i in range(1, n + 1):
    prev = dp[0]
    dp[0] = i
    for j in range(1, m + 1):
        temp = dp[j]
        if s[i - 1] == t[j - 1]:
            dp[j] = prev
        else:
            dp[j] = 1 + min(prev, dp[j], dp[j - 1])
        prev = temp

print(dp[m])
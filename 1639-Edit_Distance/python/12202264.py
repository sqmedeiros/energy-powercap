s1 = input().strip()
s2 = input().strip()

n = len(s1)
m = len(s2)


if n < m:
    s1, s2 = s2, s1
    n, m = m, n

dp = list(range(m + 1))

for i in range(1, n + 1):
    prev = dp[0]

    dp[0] = i
    for j in range(1, m + 1):
        temp = dp[j]
        # prev = dp[j - 1]
        cost = 0 if s1[i - 1] == s2[j - 1] else 1
        dp[j] = min(
            temp + 1, # delete
            dp[j - 1] + 1, #insert
            prev + cost # replace
        )
        prev = temp

print(dp[m])
s = input().strip()
t = input().strip()

n = len(s)
m = len(t)

# dp[j] = edit distance between s[:i] and t[:j]
dp_prev = list(range(m + 1))
dp_curr = [0] * (m + 1)

for i in range(1, n + 1):
    dp_curr[0] = i
    for j in range(1, m + 1):
        cost = 0 if s[i-1] == t[j-1] else 1

        dp_curr[j] = min(
            dp_prev[j] + 1,        # delete from s
            dp_curr[j-1] + 1,      # insert into s
            dp_prev[j-1] + cost    # match or replace
        )

    dp_prev, dp_curr = dp_curr, dp_prev   # swap rows

print(dp_prev[m])
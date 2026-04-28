import sys
sys.setrecursionlimit(10**7)
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

n, m = len(s), len(t)

# dp[j] = distance for previous row
prev = list(range(m + 1))
curr = [0] * (m + 1)

for i in range(1, n + 1):
    curr[0] = i
    si = s[i - 1]
    for j in range(1, m + 1):
        if si == t[j - 1]:
            curr[j] = prev[j - 1]
        else:
            curr[j] = 1 + min(
                prev[j],     # delete
                curr[j - 1], # insert
                prev[j - 1]  # replace
            )
    prev, curr = curr, prev

print(prev[m])
s = input().strip()
t = input().strip()

n, m = len(s), len(t)
prev = list(range(m + 1))
cur = [0] * (m + 1)

for i in range(1, n + 1):
    cur[0] = i
    si = s[i - 1]
    for j in range(1, m + 1):
        cost = 0 if si == t[j - 1] else 1
        cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost)

    prev, cur = cur, prev
print(prev[m])
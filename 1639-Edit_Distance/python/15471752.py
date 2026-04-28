import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

n, m = len(s), len(t)

prev = list(range(m + 1))
cur = [0] * (m + 1)

for i in range(1, n + 1):
    cur[0] = i
    for j in range(1, m + 1):
        ins = cur[j - 1] + 1
        delete = prev[j] + 1
        replace = prev[j - 1] + (0 if s[i - 1] == t[j - 1] else 1)
        cur[j] = min(ins, delete, replace)
    prev, cur = cur, prev

print(prev[m])
# end
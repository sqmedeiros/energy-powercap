a = input().strip()
b = input().strip()

n = len(a)
m = len(b)

prev = list(range(m + 1))
cur = [0] * (m + 1)

for i in range(1, n + 1):
    cur[0] = i
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            cur[j] = prev[j - 1]
        else:
            cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])
    prev, cur = cur, prev

print(prev[m])
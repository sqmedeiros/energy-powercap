from collections import deque

n, m = [int(x) for x in input().split()]

adj = [[] for _ in range(n)]
for i in range(m):
    a, b = [int(x) for x in input().split()]
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

q = deque()
q.append(0)
seen = set()
seen.add(0)
prev = [-1] * n

while q:
    c = q.popleft()
    if c == n - 1:
        break
    for out in adj[c]:
        if out not in seen:
            seen.add(out)
            prev[out] = c
            q.append(out)

if prev[n - 1] == -1:
    print("IMPOSSIBLE")
    exit(0)

cur = n - 1
path = []
while cur != 0:
    path.append(str(cur + 1))
    cur = prev[cur]
path.append("1")
print(len(path))
print(" ".join(path[::-1]))
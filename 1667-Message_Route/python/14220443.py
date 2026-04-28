import sys
from collections import deque

# input = sys.stdin.readline

n, m = map(int, input().split())

adj_list = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())

    adj_list[a].append(b)
    adj_list[b].append(a)

dist = [-1] * (n + 1)
dist[1] = 1

prev = [-1] * (n + 1)

queue = deque([1])

while queue:
    node = queue.popleft()

    if node == n:
        break

    for v in adj_list[node]:
        if dist[v] == -1:
            dist[v] = dist[node] + 1
            prev[v] = node
            queue.append(v)

if dist[-1] == -1:
    print('IMPOSSIBLE')
    sys.exit()

print(dist[-1])
ans = []
cur = n

while cur != -1:
    ans.append(cur)
    cur = prev[cur]

print(*ans[::-1])
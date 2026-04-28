import sys
sys.setrecursionlimit(3000000)
from collections import deque

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n + 1)
reps = []  # представители компонент

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        x = queue.popleft()
        for nei in adj[x]:
            if not visited[nei]:
                visited[nei] = True
                queue.append(nei)

for i in range(1, n+1):
    if not visited[i]:
        reps.append(i)
        bfs(i)

# reps содержит по одному городу из каждой компоненты
k = len(reps) - 1
print(k)

for i in range(k):
    print(reps[i], reps[i+1])
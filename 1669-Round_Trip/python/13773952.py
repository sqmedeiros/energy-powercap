n, m = map(int, input().split())
from collections import defaultdict, deque
from sys import maxsize as INF

adj = defaultdict(list)

for _ in range(m):
 a, b = map(int, input().split())
 adj[a].append(b)
 adj[b].append(a)

visited = [False] * (n + 1)
parent = [0] * (n + 1)

def dfs():
 for start in range(1, n + 1):
  if visited[start]: continue

  stack = [(start, -1)]
  while stack:
   node, par = stack.pop()

   if visited[node]: continue
   visited[node] = True
   parent[node] = par

   for neighbour in adj[node]:
    if neighbour == par: continue
    if not visited[neighbour]:
     stack.append((neighbour, node))
    if visited[neighbour]:
     cycle = [neighbour]
     cur = node
     while cur != neighbour and cur != 0:
      cycle.append(cur)
      cur = parent[cur]
     cycle.append(neighbour)
     print(len(cycle))
     print(*cycle)
     return True
 return False

if not dfs(): print("IMPOSSIBLE")
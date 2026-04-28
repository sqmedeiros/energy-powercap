from collections import defaultdict, deque
import sys
sys.setrecursionlimit(2 ** 30)

n, m = map(int, input().strip().split())

graph = defaultdict(list)
for _ in range(m):
 a, b = map(int, input().strip().split())
 graph[a].append(b)
 graph[b].append(a)

def bfs(start, target): 
 q = deque([start])
 visited = set([start])
 parent = [None] * (n + 1)

 while q:
  node = q.popleft()
  if node == target:
   return parent

  for neigh in graph[node]:
   if neigh not in visited:
    visited.add(neigh)
    q.append(neigh)
    parent[neigh] = node

ans = bfs(1, n)
if ans is not None:
 path = [n]
 while ans[path[-1]] != 1:
  path.append(ans[path[-1]])
 path.append(1)
 print(len(path))
 print(" ".join(map(str, reversed(path))))
else:
 print("IMPOSSIBLE")

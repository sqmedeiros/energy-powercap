from collections import deque

n, m = map(int, input().split())
adj = [[] for i in range(n)]

for _ in range(m):
 u, v = map(int, input().split())

 adj[u - 1].append(v - 1)
 adj[v - 1].append(u - 1)

color = [-1] * n
ok = True


def bfs(start):
 global ok

 todo = deque([(start, 0)])

 while todo:
  u, c = todo.popleft()
  color[u] = c

  for v in adj[u]:
   if color[v] == -1:
    todo.append((v, 1 - c))
   elif color[v] == c:
    # contradiction!
    ok = False
    return


for i in range(n):
 if color[i] == -1:
  bfs(i)

if ok:
 for i in range(n):
  print(color[i] + 1, end=" ")

else:
 print("IMPOSSIBLE")
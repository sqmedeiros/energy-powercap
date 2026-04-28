from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
  v, u = map(int, input().split())
  v-=1
  u-=1
  adj[v].append(u)
  adj[u].append(v)

pred = [-1]*n
vis = [False]*n
queue = deque()

vis[0] = True
queue.append(0)
while queue:
  node = queue.popleft()
  for viz in adj[node]:
    if not vis[viz]:
      vis[viz] = True
      pred[viz] = node
      queue.append(viz)

if pred[n-1] == -1:
  print("IMPOSSIBLE")
else:
  ans = [n]
  node = n-1
  while pred[node]!=-1:
    node = pred[node]
    ans.append(node+1)

  ans.reverse()
  print(len(ans))
  print(*ans, sep = " ")
from collections import deque

N, M = map(int, input().split())

neighbors = [[] for _ in range(N + 1)]

for _ in range(M):
 a, b = map(int, input().split())
 neighbors[a].append(b)
 neighbors[b].append(a)

teams = [0] * (N + 1)

is_bipartite = True
for i in range(1, N + 1):
 if teams[i] == 0:
  teams[i] = 1
  queue = deque([i])

  while queue:
   u = queue.popleft()
   current_team = teams[u]
   opposite_team = 3 - current_team

   for v in neighbors[u]:
    if teams[v] == 0:
     teams[v] = opposite_team
     queue.append(v)
    elif teams[v] == current_team:
     is_bipartite = False
     break

   if not is_bipartite:
    break
if not is_bipartite:
 print("IMPOSSIBLE")
else:
 print(" ".join(map(str, teams[1:])))

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
 a, b = map(int, input().split())
 adj[a].append(b)
 adj[b].append(a)
V = [0] * (n+1)
B = []
for i in range(1, n+1):
 if V[i]: continue
 if i != 1: B.append((i))
 Q = [i]
 while Q:
  i = Q.pop()
  for j in adj[i]:
   if not V[j]:
    V[j] = 1
    Q.append(j)
print(len(B))
for p in B: print(f'1 {p}')
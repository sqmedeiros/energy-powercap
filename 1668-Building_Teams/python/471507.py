n, m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
 a, b = map(lambda s: int(s)-1, input().split())
 adj[a].append(b)
 adj[b].append(a)
col = [0] * n
for i in range(n):
 if col[i] != 0: continue
 col[i] = 1
 Q = [i]
 while Q:
  i = Q.pop()
  for j in adj[i]:
   if col[j] == col[i]:
    print('IMPOSSIBLE')
    raise SystemExit
   elif col[j] == 0:
    col[j] = 1 if col[i] == 2 else 2
    Q.append(j)
print(*col)
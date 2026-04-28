import sys

input = sys.stdin.readline
n, m, q = map(int, input().split())
INF = 1<<59
D = [INF] * 500**2
def idx(i, j): return i + j * 500
for i in range(n): D[idx(i, i)] = 0
for _ in range(m):
 a, b, c = map(int, input().split())
 a -= 1; b -= 1
 if c < D[idx(a, b)]:
  D[idx(a, b)] = D[idx(b, a)] = c
for k in range(n):
 for i in range(n):
  d1 = D[idx(i, k)]
  if k == i or d1 == INF: continue
  for j in range(i):
   t = d1 + D[idx(k, j)]
   if t < D[idx(i, j)]:
    D[idx(i, j)] = D[idx(j, i)] = t
ans=[]
for _ in range(q):
 a, b = map(int, input().split())
 d = D[idx(a-1, b-1)]
 ans.append(d if d != INF else -1)
for i in ans:print(i)
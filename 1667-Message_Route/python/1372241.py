from collections import*
I=lambda:map(int,input().split())
P=print
n,m=I()
G=[[-1]for _ in [0]*-~n]
for _ in[0]*m:
 a,b=I()
 G[a]+=b,
 G[b]+=a,
V={1}
E=deque(V)
while E:
 for _ in[0]*len(E):
  s=E.popleft()
  if s==n:
   _=1
   break
  for e in G[s][1:]:
   if e not in V:
    V|={e}
    E+=e,
    G[e][0]=s
 if _:
  B=[s]
  while-~G[s][0]:
   s=G[s][0]
   B+=s,
  P(len(B))
  P(*B[::-1])
  exit()
P("IMPOSSIBLE")
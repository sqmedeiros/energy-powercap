from collections import defaultdict
def f(n,m,c):
 g=defaultdict(list)
 for a,b in c:
  g[a]+=[b]
  g[b]+=[a]
 v,p=[0]*(n+1),[-1]*(n+1)
 q=[1]
 v[1]=1
 while q:
        u = q.pop(0)
        if u == n:
            break
        for x in g[u]:
            if not v[x]:
                q += [x]
                v[x] = 1
                p[x] = u

 if not v[n]:
        return
 else:
        route = []
        x = n
        while x != -1:
            route += [x]
            x = p[x]
        return len(route), reversed(route)
n,m=map(int,input().split())
c=[tuple(map(int,input().split()))for _ in range(m)]
r=f(n,m,c)
if r:
 l,g=r
 print(l)
 print(*g)
else:
 print("IMPOSSIBLE")
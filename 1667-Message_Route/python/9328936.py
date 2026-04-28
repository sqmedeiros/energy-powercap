I=lambda:map(int,input().split())
P=print
n,m=I()
p=[0]*n*2
g=[[]for _ in p]
for _ in " "*m:
 a,b=I()
 g[a]+=b,
 g[b]+=a,
q=[n]
v={n}
d={n:1}
for u in q:
 for x in g[u]:
  if {x}-v:
   q += [x]
   v|={x}
   p[x] = u 
   d[x] = d[u] + 1
if {1}-v:
 P("IMPOSSIBLE")
else:
 u = 1
 P(d[1])
 while u:
  P(u)
  u=p[u]
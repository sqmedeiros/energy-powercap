from collections import*
n,m=map(int,input().split())
g=defaultdict(list)
for _ in[0]*m:a,b=map(int,input().split());g[a]+=[b];g[b]+=[a]
i=n+1
q=[1]
v,p=q*i,[-1]*i
v[1]=0
while q:
 u=q.pop(0)
 if u==n:
  break
 for x in g[u]:
  if v[x]:
   q+=[x]
   v[x],p[x]=0,u
if v[n]<1:
 y=[]
 while n!=-1:
  y+=[n]
  n=p[n]
 print(len(y),*y[::-1])
else:
 print("IMPOSSIBLE")
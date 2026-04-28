n,m=map(int,input().split())
h=[0]
i=n+1
g=[[]for _ in h*i]
for _ in h*m:a,b=map(int,input().split());g[a]+=[b];g[b]+=[a]
q=[1]
v,p=q*i,h*i
v[1]=0
while q:
 u=q.pop(0)
 if v[n]<1:
  y=[]
  while n:
   y+=[n]
   n=p[n]
  print(len(y),*y[::-1])
  exit()
 for x in g[u]:
  if v[x]:
   q+=[x]
   v[x],p[x]=0,u
print("IMPOSSIBLE")
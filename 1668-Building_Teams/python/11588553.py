import sys; input=sys.stdin.readline
n,m=map(int,input().split())
g=[[] for j in range(n)]
for j in range(m):
  u,v=map(int,input().split())
  g[u-1].append(v-1)
  g[v-1].append(u-1)
out=[0]*n
vis=[0]*n
s=[]
check=1
for j in range(n):
  if not(vis[j]):
    s.append(j)
    vis[j]=1
    out[j]=1
    while s:
      parent=s.pop()
      for child in g[parent]:
        if not(vis[child]):
          vis[child]=1
          s.append(child)
          out[child]=(1 if out[parent]==2 else 2)
        else:
          if out[parent]==out[child]:
            check=0
if check:
  print(*out)
else:
  print('IMPOSSIBLE')
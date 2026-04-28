import sys
sys.setrecursionlimit(100000)
n,m=map(int,input().split())
l=[1]*n
g=[[] for i in range(n)]
def dfs(x):
 l[x]=0
 for q in g[x]:
  if l[q]:
   dfs(q)
for i in range(m):
 u,v=map(int,input().split())
 u-=1
 v-=1
 g[u].append(v)
 g[v].append(u)
o=[]
for i in range(n):
 if l[i]:
  dfs(i)
  o+=[i+1]
print(len(o)-1)
for i in range(1,len(o)):
 print(o[i-1], o[i])
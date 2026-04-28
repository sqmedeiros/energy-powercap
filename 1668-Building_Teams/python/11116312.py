n,m=(int(i) for i in input().split())
adj=[[] for i in range(n)]
for i in range(m):
 a,b=(int(x) for x in input().split())
 adj[a-1].append(b-1)
 adj[b-1].append(a-1)
col=[None]*n
def dfs(src):
 s=[src]
 col[src]=1
 while s:
  i=s.pop()
  for j in adj[i]:
   if col[j] is None:
    col[j]=1+col[i]%2
    s.append(j)
   elif col[j]==col[i]:
    return -1
 return 0
for i in range(n):
 if col[i] is None:
  if dfs(i)==-1:
   print('IMPOSSIBLE')
   break
else:
 print(' '.join(map(str,col)))
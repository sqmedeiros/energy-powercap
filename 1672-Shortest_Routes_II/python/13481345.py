import sys
input = sys.stdin.readline
n,m,q=map(int,input().split())
INF=10**18
d=[[INF]*n for _ in range(n)]
for i in range(n):d[i][i]=0
for _ in range(m):
 a,b,c=map(int,input().split())
 a-=1;b-=1
 if c<d[a][b]:d[a][b]=d[b][a]=c
for k in range(n):
 dk=d[k]
 for i in range(n):
  di=d[i];vik=di[k]
  for j in range(n):
   if vik+dk[j]<di[j]:di[j]=vik+dk[j]
w=sys.stdout.write
for _ in range(q):
 a,b=map(int,input().split())
 a-=1;b-=1
 x=d[a][b]
 w(f"{x if x<INF else -1}\n")
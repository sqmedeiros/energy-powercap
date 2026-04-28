import sys; input=sys.stdin.readline
n,x=map(int,input().split())
a=list(map(int,input().split()))
d=dict()
f=1
for j in range(n):
  for k in range(j+1,n):
    if x-a[j]-a[k] in d:
      print(d[x-a[j]-a[k]][0],d[x-a[j]-a[k]][1],j+1,k+1)
      f=0
      break
  if not(f):
    break
  for k in range(j):
    d[a[j]+a[k]]=(k+1,j+1)
if f:
  print('IMPOSSIBLE')
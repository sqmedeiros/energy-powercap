import sys
n,x = map(int,input().split())
a = sorted([int(i) for i in input().split()])
inf = 10**9
f = [inf]*(x+1)
f[0] = 0
for i in range(1,x+1): 
  for j in a: 
    if i-j < 0: break
    f[i]= min(f[i],f[i-j]+1)
if f[x] == inf: print('-1')
else: print(f[x])
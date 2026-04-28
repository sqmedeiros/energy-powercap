import sys
I=lambda:map(int,sys.stdin.readline().split())
n,m,q=I()
n+=1
f=2**39
T=n*n*[f]
N=range(n)
for i in N:T[i*-~n]=0
for _ in" "*m:
 a,b,c=I()
 A=a*n+b
 T[A]=T[b*n+a]=min(T[A],c)
for k in N:
 k*=n
 for a in N:
  A=a*n
  for b in N:T[A+b]=min(T[A+b],T[k+a]+T[k+b])
for _ in" "*q:
 a,b=I()
 print((f!=T[a*n+b])*-~T[a*n+b]-1)
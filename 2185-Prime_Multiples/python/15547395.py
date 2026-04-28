import sys
it=iter(sys.stdin.read().strip().split())
n=int(next(it));k=int(next(it))
p=[int(next(it)) for _ in range(k)]
lim=n
N=1<<k
prods=[1]*N
for m in range(1,N):
    lb=m&-m
    i=(lb.bit_length()-1)
    prev=m^lb
    v=prods[prev]*p[i]
    prods[m]=v if v<=lim else lim+1
ans=0
for m in range(1,N):
    if prods[m]>lim: continue
    cnt=n//prods[m]
    if bin(m).count("1")%2: ans+=cnt
    else: ans-=cnt
print(ans)
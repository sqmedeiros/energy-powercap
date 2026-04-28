I=lambda:map(int,input().split())
M=max
n,q=I()
P=*W,=2*n*[0]
def U(i):
 P[i]=W[i]=e
 while i>1:
  i>>=1
  j=2*i
  P[i]=M(W[j]+P[j^1],P[j])
  W[i]=W[j]+W[j^1]
i=n
for e in I():
 U(i)
 i+=1
while q:
 q-=1
 t,s,e=I()
 s+=n-1
 if t>1or U(s):
  a=b=c=0
  S=s
  E=e=e+n
  while S<E:
   b+=S%2*W[S]
   b+=E%2*W[E-1]
   S=S+1>>1
   E>>=1
  while s<e:
   if s&1:
    c=M(c,a+P[s])
    a+=W[s]
    s+=1
   if e&1:
    e-=1
    b-=W[e]
    c=M(c,b+P[e])
   s>>=1
   e>>=1
  print(c)
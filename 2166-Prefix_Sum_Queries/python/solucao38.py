I=lambda:map(int,input().split())
n,q=I()
P=*W,=2*n*[0]
def U(i):
    P[i]=W[i]=e
    while i>1:
        i>>=1
        j=2*i
        P[i]=max(W[j]+P[j^1],P[j])
        W[i]=W[j]+W[j^1]
b=n
for e in I():
    U(b)
    b+=1
while q:
    q-=1
    a,s,e=I()
    s+=n-1
    if a>1or U(s):
        a=s
        b=0
        c=e=e+n
        while a<c:
            b+=a%2*W[a]
            b+=c%2*W[c-1]
            a=a+1>>1
            c>>=1
        a=c=0
        while s<e:
            if s&1:
                c=max(c,a+P[s])
                a+=W[s]
                s+=1
            if e&1:
                e-=1
                b-=W[e]
                c=max(c,b+P[e])
            s>>=1
            e>>=1
        print(c)
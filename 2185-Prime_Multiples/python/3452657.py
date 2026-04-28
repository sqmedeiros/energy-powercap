I=lambda:map(int,input().split())
R=range
n,k=I()
*p,=I()
a=0
for m in R(1,1<<k):
    x=c=1
    for j in R(k):
        if m&2**j:
            x*=p[j]
            c+=1
    a+=n//x*(-1)**c
print(a)
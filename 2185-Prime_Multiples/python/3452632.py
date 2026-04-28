I=input
n,k=map(int,I().split())
p=list(map(int,I().split()))
a=0
for m in range(1,1<<k):
    x=c=1
    for j in range(k):
        if m&(1<<j):
            x*=p[j]
            c+=1
    a+=n//x*(-1)**c
print(a)
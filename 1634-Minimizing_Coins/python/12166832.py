I=lambda:map(int,input().split())
n,x = I()
k=x+2
l=[1]+[k]*k
for c in I():
    i=c
    while i<k:
        l[i]=min(l[i],1+l[i-c])
        i+=1
print(l[x]%k-1)

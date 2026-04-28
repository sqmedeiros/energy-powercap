import sys, collections

d=list(map(int,sys.stdin.buffer.read().split()))
n,x=d[0],d[1]
a=d[2:]

seen=collections.defaultdict(list)
for i in range(n):
    ai=a[i]
    for j in range(i+1,n):
        s=ai+a[j]
        need=x-s
        if need in seen:
            for p,q in seen[need]:
                if p!=i and p!=j and q!=i and q!=j:
                    print(p+1,q+1,i+1,j+1)
                    sys.exit()
        seen[s].append((i,j))
print("IMPOSSIBLE")
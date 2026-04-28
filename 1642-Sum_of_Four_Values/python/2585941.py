N,T=map(int,input().split())
A=list(map(int,input().split()))
B=[]
for idx,a in enumerate(A):
    B.append([a,idx+1])

def find(A,N,T):
    hash={}
    for i in range(N-1):
        a=A[i]
        for j in range(i+1,N):
            b=A[j]
            hash[a[0]+b[0]]=[a[1],b[1]]
    for i in range(N-1):
        a=A[i]
        for j in range(i+1,N):
            b=A[j]
            s=a[0]+b[0]
            comp=T-s
            if comp in hash:
                c,d=hash[comp]
                if a[1] not in hash[comp] and b[1] not in hash[comp]:
                    return [a[1],b[1],c,d]
    return []

ans=find(B,N,T)
if ans:
    print(" ".join(map(str,ans)))
else:
    print("IMPOSSIBLE")
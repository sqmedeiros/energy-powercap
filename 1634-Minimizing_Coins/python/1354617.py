I=lambda:map(int,input().split())
O=10**7
_,x=I()
*C,=I()
A=[1]+[O]*(x+max(C))
for i in range(x):
 for c in C:A[i+c]=min(A[i+c],A[i]+1)
print((A[x]!=O)*A[x]-1)
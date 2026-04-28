I=lambda:map(int,input().split())
_,x=I()
*C,=I()
A=[1]+[0]*(x+max(C))
for i in range(x):
 for c in C:
  A[i+c]+=A[i]
  A[i+c]%=10**9+7
print(A[x])
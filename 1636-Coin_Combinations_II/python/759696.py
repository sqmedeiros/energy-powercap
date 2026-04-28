m=lambda:map(int,input().split())
n,x=m()
*d,=1,*[0]*x
for c in m():
    for i in range(c,-~x):
        d[i]+=d[i-c]
        d[i]%=10**9+7
print(d[x])
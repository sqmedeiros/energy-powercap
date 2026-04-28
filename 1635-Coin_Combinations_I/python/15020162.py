n, x= map(int, input().split())
c= list(map(int, input().split()))
l=[1]+[0]*7**8
for i in range(x+1):
    l[i]%=10**9+7
    for k in c:
        l[i+k]+=l[i]
print(l[x])

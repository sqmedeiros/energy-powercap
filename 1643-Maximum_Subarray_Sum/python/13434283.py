n=int(input())
a=list(map(int , input().split()))
res=a[0]
endWith=a[0]
res=a[0]
for i in range(1,n):
    endWith=max(endWith+a[i],a[i])
    if endWith > res :
        res=endWith
print(res)
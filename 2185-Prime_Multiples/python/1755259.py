def construct(a,c,n,k,num,pick,i):
    if i == k:
        c[pick - 1] += (n // num)
        return
    construct(a,c,n,k,num,pick,i+1)
    construct(a,c,n,k,num * a[i],pick + 1,i+1)
    return


n,k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
c = [0] * k
for i in range(k):
    construct(a,c,n,k,a[i],1,i+1)
ans = 0
for i in range(0,k,2):
    ans += c[i]
for i in range(1,k,2):
    ans -= c[i]
print(ans)
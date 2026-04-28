def count_bits(n):
    c=0
    while n!=0:
        n=n&(n-1)
        c+=1
    return c
n,k=map(int, input().split())
a=list(map(int, input().split()))
s=0
md=10**9+7
for i in range(1, 2**k):
    c = count_bits(i)

    num=1
    for j in range(k):
        if i&(1<<j):
            num = (num*a[j])
        if num > n:
            break
    if num > n:
        continue
    s = s + (n//num)*(1 if c%2 else -1)
print(s)




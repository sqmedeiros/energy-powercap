n, k = map(int, input().split())
a = list(map(int, input().split()))
res = 0

limit = (1 << k) - 1  

for mask in range(1, limit + 1):
    product = 1
    overflow = False
    for i in range(k):
        if mask & (1 << i):
            if product > n // a[i]:  
                overflow = True
                break
            product *= a[i]
    if overflow or product > n:
        continue
    bits = bin(mask).count('1')  
    if bits % 2:
        res += n // product
    else:
        res -= n // product

print(res)

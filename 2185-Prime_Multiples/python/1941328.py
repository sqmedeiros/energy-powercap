n, k = input().split()
n, k = int(n), int(k)

a = list(map(int, input().split()))

res = 0
for i in range(1, 1 << k):
    prod = 1
    parr = -1
    for j in range(k):
        if i & (1 << j):
            if prod <= n:
                prod *= a[j]
            parr = -parr
    res += parr * (n // prod)

print(res)
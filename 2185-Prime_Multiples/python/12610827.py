def cnt(x):
    c = 0
    while x:
        c += x & 1
        x >>= 1
    return c
n, k = map(int, input().split())
ans = 0
a = list(map(int, input().split()))
for i in range(1, 1 << k):
    x = 1
    for j in range(k):
        if i & (1 << j):
            x *= a[j]
    if cnt(i) & 1:
        ans += n // x
    else:
        ans -= n // x
print(ans)
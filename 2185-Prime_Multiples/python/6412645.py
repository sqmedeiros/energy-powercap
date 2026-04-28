def cnt(i):
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24
n, k = map(int, input().split())
a = [*map(int, input().split())]
M = 1 << k
ans = 0
for i in range(1, M):
    p = 1
    for j, x in enumerate(a):
        if i & (1 << j):
            if p > n // x:
                p = n + 1
                break
            p = p * x
    c = cnt(i)
    if c & 1:
        ans += n // p 
    else:
        ans -= n // p
print(ans)
n, k = map(int, input().split())
ans = 0
a = [int(i) for i in input().split()]
for mask in range(1, 2 ** k):
    bits, curr = 0, 1
    for i in range(k):
        if mask & (2 ** i) != 0:
            bits += 1
            curr *= a[i]
    if bits % 2 == 1: ans += n // curr
    else: ans -= n // curr
print(ans)
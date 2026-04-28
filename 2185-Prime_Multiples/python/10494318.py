n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = n

for i in range(1 << k):
    selected = [a[j] for j in range(k) if i & (1 << j)]
    prod = 1
    for val in selected:
        prod *= val
        if prod > n:
            continue
    if len(selected) & 1:
        ans += n // prod
    else:
        ans -= n // prod

print(ans)
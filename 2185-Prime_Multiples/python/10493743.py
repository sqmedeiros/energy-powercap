n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = n

for i in range(1 << k):
    selected = [a[j] for j in range(k) if i & (1 << j)]
    prod = 1
    for val in selected:
        prod *= val

    if len(selected) % 2:
        ans += n // prod
    else:
        ans -= n // prod

print(ans)
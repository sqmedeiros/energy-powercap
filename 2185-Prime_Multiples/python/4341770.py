n, k = map(int, input().split())

a = list(map(int, input().split()))

ans = 0
for i in range(1, 1 << k):
    val = 1
    cnt = 0
    for j in range(k):
        if ((1 << j) & i) > 0:
            val *= a[j]
            cnt += 1
    if cnt % 2 == 1:
        ans += n // val
    else:
        ans -= n // val

print(ans)
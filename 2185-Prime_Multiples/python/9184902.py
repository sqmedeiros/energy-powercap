n, m = map(int, input().split())

arr = list(map(int, input().split()))

res = 0
for i in range(1, 1 << m):
    curr = 1
    pref = 0
    for j in range(m):
        if i & (1 << j):
            curr *= arr[j]
            if curr > n:
                break
            pref += 1

    if pref % 2 == 0:
        res -= n // curr
    else:
        res += n // curr

print(res)
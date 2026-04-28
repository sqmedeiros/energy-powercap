n, k = map(int, input().split())
a = list(map(int, input().strip().split()))[:k+1]
ans = 0
for mask in range(1, (1 << k)):
    x = 1
    cnt = 0
    for i in range(0, k):
        if(mask >> i & 1):
            x *= a[i]
            cnt = cnt + 1
    if(cnt & 1):
        ans += n // x
    else:
        ans -= n // x
print(ans)
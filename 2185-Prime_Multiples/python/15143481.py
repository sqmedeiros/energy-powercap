n, k = map(int, input().split())
p = list(map(int, input().split()))
res = 0 
for i in range(1, 1 << k):
    cnt = 0 
    num = 1 
    for j in range(k):
        if i & (1 << j): 
            cnt += 1 
            num *= p[j]
    if cnt % 2:
        res += n // num
    else:
        res -= n // num 
print(res)
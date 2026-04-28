n, k = map(int, input().split())
primes = list(map(int, input().split()))

ans = 0
for mask in range(1, 1 << k):
    lcm1 = 1
    cant = 0
    ok = True
    for i in range(k):
        if mask & (1 << i):
            cant += 1
            if lcm1 > n // primes[i]:
                ok = False
                break
            lcm1 *= primes[i]
    if not ok:
        continue
    if cant % 2 == 1:
        ans += n // lcm1
    else:
        ans -= n // lcm1

print(ans)
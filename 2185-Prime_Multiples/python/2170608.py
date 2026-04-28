n, k = map(int, input().split())
primes = list(map(int, input().split()))
ans = 0
for mask in range(0, 2 ** k):
    cont, all = 0, 1
    for i in range(0, k):
        if mask & (2 ** i) != 0:
            all *= primes[i]
            cont += 1
    if cont == 0:
        continue
    if cont%2:
        ans += n // all
    else:
        ans -=  n // all
print(ans)
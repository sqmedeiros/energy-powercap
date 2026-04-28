n, k = map(int, input().split())
primes = list(map(int, input().split()))

total = 0

for mask in range(1, 1 << k):
    bits = bin(mask).count('1')
    product = 1
    overflow = False
    for i in range(k):
        if mask & (1 << i):
            if product > n // primes[i]:
                overflow = True
                break
            product *= primes[i]
    if overflow:
        continue
    if bits % 2 == 1:
        total += n // product
    else:
        total -= n // product

print(total)
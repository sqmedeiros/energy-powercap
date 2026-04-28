from itertools import combinations

n, k = map(int, input().split())
primes = list(map(int, input().split()))
total = 0
for i in range(1, k + 1):
    for subset in combinations(primes, i):
        product = 1
        for num in subset:
            product *= num
            if product > n:
                break
        if product > n:
            continue
        count = n // product
        if i % 2 == 1:
            total += count
        else:
            total -= count

print(total)
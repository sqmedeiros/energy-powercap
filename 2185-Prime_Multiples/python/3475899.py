from itertools import combinations
from functools import reduce
import operator

def product(iter):
    return reduce(operator.mul, iter, 1)


n, k = map(int, input().split())

primes = list(map(int, input().split()))

total = 0
alt = 1
for r in range(1, k+1):
    for t in combinations(primes, r):
        total += alt * (n // product(t))
    alt *= -1

print(total)
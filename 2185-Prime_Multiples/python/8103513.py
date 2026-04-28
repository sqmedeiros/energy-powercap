from itertools import combinations

def count_divisible_numbers(n, primes):
    result = 0

    for j in range(1, len(primes) + 1):
        for combination in combinations(primes, j):
            lcm = 1
            for prime in combination:
                lcm *= prime

            if j % 2 == 1:
                result += n // lcm
            else:
                result -= n // lcm

    return result

n, k = map(int, input().split())
primes = list(map(int, input().split()))

result = count_divisible_numbers(n, primes)
print(result)
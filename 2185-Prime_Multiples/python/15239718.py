n, k = map(int, input().split())
primes = list(map(int, input().split()))

result = 0

for mask in range(1, 1 << k):
    count = 0
    lcm = 1

    for i in range(k):
        if mask & (1 << i):
            count += 1
            if lcm > n // primes[i]:
                lcm = n + 1
                break
            lcm *= primes[i]

    divisible_count = n // lcm

    if count % 2 == 1:
        result += divisible_count
    else:
        result -= divisible_count

print(result)
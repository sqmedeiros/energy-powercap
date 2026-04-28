n, k = map(int, input().split())
primes = [int(i) for i in input().split()]
total = 0
k = len(primes)

# Using bitwise operations to iterate through all subsets of primes
for subset in range(1, 1 << k):
    subset_product = 1
    num_primes = 0

     # Iterate through each bit of subset
    for i in range(k):
        if subset & (1 << i):
            subset_product *= primes[i]
            num_primes += 1

     # If the number of primes in the subset is odd, add, else subtract
    if num_primes % 2:
        total += n // subset_product
    else:
        total -= n // subset_product

print(total)
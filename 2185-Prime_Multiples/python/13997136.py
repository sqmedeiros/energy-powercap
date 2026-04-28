def countDivisible(arr, m):
    n = len(arr)
    odd = 0
    even = 0

    # Total subsets = 2^n (including empty set)
    powerSet = 1 << n

    # Iterate through all non-empty subsets of primes
    for mask in range(1, powerSet):
        product = 1
        bitCount = 0  

        # Compute the product of selected primes in this subset
        for j in range(n):
            if mask & (1 << j):
                product *= arr[j]
                bitCount += 1

                # If product exceeds m, break early
                if product > m:
                    break

        # If product exceeds m, skip this subset
        if product > m:
            continue

        count = m // product

        # Inclusion-Exclusion:
        # - If number of selected primes is odd, add the count
        # - If even, subtract the count
        if bitCount % 2 == 1:
            odd += count
        else:
            even += count
    return odd - even


if __name__ == "__main__":
    n, k = map(int, input().split())
    primes = list(map(int, input().split()))
    print(countDivisible(primes, n))
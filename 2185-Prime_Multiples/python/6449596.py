def main():
    range_length, prime_count = map(int, input().split())
    primes = list(map(int, input().split()))

    multiples = 0

    # Bitmasks are binary representations of subsets, in which the nth bit is 1 if and only if the nth value is used.
    for bitmask in range(1, 1 << prime_count): # 1 << n = 2 ** n because in binary, 2 ** n is 1 followed by n zeros, which is the same as 1 shifted n bits to the right.
        length, number = 0, 1

        for index, prime in enumerate(primes):
            if not (bitmask & (1 << index)): # 1 << i has a 1 only at index i, so this as if the ith bit is on in the bitmask.
                continue

            number *= prime
            length += 1

        multiples_found = range_length // number
        multiples += multiples_found if length % 2 == 1 else -multiples_found # Inclusion-Exclusion Principle (PIE)

    print(multiples)

if __name__ == "__main__":
    main()
def main():

    n, k = map(int, input().split())
    primes = list(map(int, input().split()))

    count = 0
    # Cada subconjunto de primos é representado por um número de 1 a (1<<k)-1
    for mask in range(1, 1 << k):
        mult = 1
        bits = 0
        for j in range(k):
            if mask & (1 << j):
                bits += 1
                mult *= primes[j]
                if mult > n:  # não precisa continuar se o produto já passou de n
                    break
        else:
            # Princípio da inclusão-exclusão
            if bits % 2 == 1:
                count += n // mult
            else:
                count -= n // mult

    print(count)

main()
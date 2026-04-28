def solve_divisibility(n, k, primes):
    """
    Calcula o número de inteiros de 1 a n divisíveis por pelo menos
    um dos k primos usando o Princípio da Inclusão-Exclusão.
     Args:
        n (int): O limite superior do intervalo.
        k (int): O número de primos.
        primes (list): Uma lista de k primos distintos.
     Returns:
        int: A contagem de números que atendem à condição.
    """
    total = 0

    # Gerar todos os subconjuntos de primos e aplicar o princípio de inclusão-exclusão
    # Usamos uma abordagem bitmask para gerar os subconjuntos, que é concisa e eficiente
    # O loop vai de 1 a 2^k - 1 para ignorar o subconjunto vazio
    for i in range(1, 1 << k):
        # bitmask 'i' representa o subconjunto atual

        # Produto dos primos no subconjunto
        current_product = 1
        # Contagem de elementos no subconjunto
        subset_size = 0

        # Iterar sobre os bits da máscara
        for j in range(k):
            # Se o j-ésimo bit estiver ligado, o j-ésimo primo está no subconjunto
            if (i >> j) & 1:
                subset_size += 1
                current_product *= primes[j]

        # Verifique se o produto não excede n para evitar overflow e otimizar
        if current_product > n:
            continue

        # Adiciona ou subtrai com base na paridade do tamanho do subconjunto
        count_multiples = n // current_product
        if subset_size % 2 == 1:
            total += count_multiples
        else:
            total -= count_multiples

    return total

n_str, k_str = input().split()
n = int(n_str)
k = int(k_str)
primes = list(map(int, input().split()))

result = solve_divisibility(n, k, primes)
print(result)
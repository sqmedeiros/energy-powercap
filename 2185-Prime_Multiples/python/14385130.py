import sys

def solve_recursive():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    total_count = 0

    # Função recursiva para explorar subconjuntos e aplicar Inclusão-Exclusão
    # index: índice do primo atual que estamos considerando incluir/excluir
    # current_product: produto dos primos incluídos até agora neste subconjunto
    # count_primes: número de primos incluídos neste subconjunto até agora
    def find_subsets(index, current_product, count_primes):
        nonlocal total_count

        # Se o produto atual já excedeu n, este caminho não contribuirá.
        # Também tratamos o caso de overflow aqui, se current_product ficar muito grande.
        if current_product > n:
            return

        # Base case: Todos os primos foram considerados
        if index == k:
            # Se já consideramos pelo menos um primo (um subconjunto não vazio)
            if count_primes > 0:
                # Se o número de primos no subconjunto for ímpar, adicionamos
                if count_primes % 2 == 1:
                    total_count += n // current_product
                # Se o número de primos no subconjunto for par, subtraímos
                else:
                    total_count -= n // current_product
            return

        # 1. Não incluir o primo a[index]
        find_subsets(index + 1, current_product, count_primes)

        # 2. Incluir o primo a[index]
        # Verificar se a multiplicação vai estourar 'n' antes de fazê-la
        if n // a[index] >= current_product: # Equivale a current_product * a[index] <= n
            find_subsets(index + 1, current_product * a[index], count_primes + 1)

    # Inicia a recursão: começando do primeiro primo (índice 0),
    # com um produto inicial de 1 e 0 primos contados.
    find_subsets(0, 1, 0)

    print(total_count)

def main():
    solve_recursive()

if __name__ == "__main__":
    main()
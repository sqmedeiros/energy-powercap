import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    bosses = list(map(int, data[1:1+n-1]))

    tree = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        boss = bosses[i-2]
        tree[boss].append(i)

    subordinates_count = [0] * (n+1)

    # Calcular a ordem topológica (níveis)
    in_degree = [0] * (n+1)
    for i in range(1, n+1):
        for child in tree[i]:
            in_degree[child] += 1

    # Fila para nós com grau de entrada zero (folhas)
    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)

    # Ordem reversa (das folhas para a raiz)
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for child in tree[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                q.append(child)

    # Processar na ordem reversa (do final para o início)
    for node in reversed(order):
        total = 0
        for child in tree[node]:
            total += subordinates_count[child] + 1
        subordinates_count[node] = total

    result = []
    for i in range(1, n+1):
        result.append(str(subordinates_count[i]))

    print(" ".join(result))

if __name__ == "__main__":
    main()
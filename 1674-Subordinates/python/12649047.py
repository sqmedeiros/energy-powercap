def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    n = int(input())
    bosses = list(map(int, input().split()))

    # Строим дерево (список смежности)
    tree = [[] for _ in range(n + 1)]
    for emp in range(2, n + 1):
        boss = bosses[emp - 2]
        tree[boss].append(emp)

    # Инициализируем массив для подсчета подчиненных
    subordinates = [0] * (n + 1)

    # Итеративный DFS с постобработкой
    stack = [(1, False)]  # (node, visited)

    while stack:
        node, visited = stack.pop()
        if visited:
            # Постобработка: считаем подчиненных
            count = 0
            for child in tree[node]:
                count += subordinates[child] + 1
            subordinates[node] = count
        else:
            # Добавляем узел обратно в стек с флагом посещения
            stack.append((node, True))
            # Добавляем детей в обратном порядке для обработки слева направо
            for child in reversed(tree[node]):
                stack.append((child, False))

    # Выводим результаты
    print(' '.join(map(str, subordinates[1:n+1])))

if __name__ == "__main__":
    main()
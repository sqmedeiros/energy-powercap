def find_components(n, graph):
    # Массив для хранения того, посещали ли мы вершину
    visited = [False] * n
    components = []

    # DFS для поиска компонент
    def dfs(v, component):
        stack = [v]
        while stack:
            u = stack.pop()
            if not visited[u]:
                visited[u] = True
                component.append(u)
                for neighbor in graph[u]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    # Поиск всех компонент
    for i in range(n):
        if not visited[i]:
            component = []
            dfs(i, component)
            components.append(component)

    return components

# Чтение входных данных
n, m = map(int, input().split())

# Построение графа как список смежности
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

# Находим все компоненты связности
components = find_components(n, graph)

# Количество дорог, которые нужно построить
k = len(components) - 1

# Вывод результата
print(k)
if k > 0:
    # Соединяем каждую компоненту с предыдущей
    for i in range(1, len(components)):
        # Берем по одному городу из каждой компоненты и соединяем их
        print(components[i-1][0] + 1, components[i][0] + 1)
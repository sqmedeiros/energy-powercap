def find_cycle(n, graph):
    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)

    def dfs(start):
        stack = [(start, -1)]  # (current_node, parent_node)
        while stack:
            v, p = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            parent[v] = p
            for u in graph[v]:
                if not visited[u]:
                    stack.append((u, v))
                elif u != p:  # Found a back edge
                    # Reconstruct the cycle
                    cycle = []
                    x = v
                    while x != u:
                        cycle.append(x)
                        x = parent[x]
                    cycle.append(u)
                    cycle.append(v)
                    cycle.reverse()
                    return cycle
        return None

    for v in range(1, n + 1):
        if not visited[v]:
            result = dfs(v)
            if result:
                return result
    return None

# Leitura da entrada
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

# Criando a lista de adjacência
graph = [[] for _ in range(n + 1)]

index = 2
for _ in range(m):
    a = int(data[index])
    b = int(data[index + 1])
    graph[a].append(b)
    graph[b].append(a)
    index += 2

# Encontrar o ciclo
cycle = find_cycle(n, graph)

# Saída
if cycle:
    print(len(cycle))
    print(' '.join(map(str, cycle)))
else:
    print("IMPOSSIBLE")
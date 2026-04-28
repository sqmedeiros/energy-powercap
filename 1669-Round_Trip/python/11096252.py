"""
Round Trip
https://cses.fi/problemset/task/1669/
 Byteland has n cities and m roads between them. Your task is to design a round trip that begins in a city, goes through two or more other cities, and finally returns to the starting city. Every intermediate city on the route has to be distinct.
Input
The first input line has two integers n and m: the number of cities and roads. The cities are numbered 1,2,\dots,n.
Then, there are m lines describing the roads. Each line has two integers a and b: there is a road between those cities.
Every road is between two different cities, and there is at most one road between any two cities.
Output
First print an integer k: the number of cities on the route. Then print k cities in the order they will be visited. You can print any valid solution.
If there are no solutions, print "IMPOSSIBLE".
Constraints
 1 \le n \le 10^5
1 \le m \le 2 \cdot 10^5
1 \le a,b \le n
 Example
Input:
5 6
1 3
1 2
5 3
1 5
2 4
4 5
 Output:
4
3 5 1 3
"""

import sys
from collections import defaultdict, deque

def find_cycle(n, m, edges):
    # Строим граф
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    cycle_start = -1
    cycle_end = -1

    # Итеративный DFS для поиска цикла
    def iterative_dfs(start):
        nonlocal cycle_start, cycle_end
        stack = [(start, -1)]  # стек для хранения города и родителя
        while stack:
            v, p = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            parent[v] = p
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    stack.append((neighbor, v))
                elif neighbor != p:
                    cycle_start = neighbor
                    cycle_end = v
                    return True
        return False

    # Запускаем итеративный DFS для каждой компоненты графа
    for i in range(1, n + 1):
        if not visited[i]:
            if iterative_dfs(i):
                break

    # Если цикл не найден, выводим "IMPOSSIBLE"
    if cycle_start == -1:
        print("IMPOSSIBLE")
    else:
        # Восстанавливаем путь цикла
        cycle = []
        v = cycle_end
        while v != cycle_start:
            cycle.append(v)
            v = parent[v]
        cycle.append(cycle_start)
        cycle.append(cycle_end)
        # Выводим результат
        print(len(cycle))
        print(" ".join(map(str, cycle)))

# Чтение входных данных
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Запуск функции для поиска цикла
find_cycle(n, m, edges)
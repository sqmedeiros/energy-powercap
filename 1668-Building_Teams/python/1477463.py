import random
from collections import defaultdict, deque

n, m = map(int, input().split())
colors = dict()

graph = defaultdict(set)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

unvisited = set(range(1, n + 1))
Q = deque([])

# for assigning colors
while unvisited or Q:
    if not Q:
        Q.append((unvisited.pop(), 'red'))

    node, color = Q.popleft()
    colors[node] = color

    for nei in graph[node]:
        if nei in unvisited:
            newColor = 'purple' if color == 'red' else 'red'
            Q.append((nei, newColor))
            unvisited.remove(nei)

# for verification
def isBipartite():
    unvisited = set(range(1, n + 1))
    Q = deque([])

    while unvisited or Q:
        if not Q:
            Q.append(unvisited.pop())

        node = Q.popleft()
        for nei in graph[node]:
            if colors[node] == colors[nei]:
                return False

            if nei in unvisited:
                Q.append(nei)
                unvisited.remove(nei)

    return True

if isBipartite():
    print(' '.join('1' if colors[i] == 'red' else '2' for i in range(1, n + 1)))
else:
    print('IMPOSSIBLE')
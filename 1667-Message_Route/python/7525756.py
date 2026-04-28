from collections import deque

def solve(graph, n):
    distance = [float('inf')] * (n + 1)
    distance[1] = 0
    parent = [-1] * (n + 1)

    heap = deque([(0, 1)])

    while heap:
        currdist, curr = heap.popleft()
        for neighbour in graph[curr]:
            if distance[neighbour] > currdist + 1:
                distance[neighbour] = currdist + 1
                parent[neighbour] = curr
                heap.append((currdist + 1, neighbour))

    if distance[n] == float('inf'):
        return (None, None)
    x = n
    path = []
    while x != 1:
        path.append(x)
        x = parent[x]
    path.append(1)
    path.reverse()
    return (distance[n] + 1, path)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)
    graph[x].append(y)

distance, path = solve(graph, n)
if not distance:
    print("IMPOSSIBLE")
else:
    print(distance)
    for i in path:
        print(i, end=" ")

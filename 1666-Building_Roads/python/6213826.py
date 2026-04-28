from queue import Queue

n, m = map(int, input().split())

adjacencies = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cities = []
queue = Queue()

for _ in range(m):
    v1, v2 = map(int, input().split())
    adjacencies[v1].append(v2)
    adjacencies[v2].append(v1)


def bfs(first):
    queue.put(first)
    visited[first] = True

    while not queue.empty():
        node = queue.get()

        for vert in adjacencies[node]:
            if not visited[vert]:
                queue.put(vert)
                visited[vert] = True


for vert in range(1, n + 1):
    if not visited[vert]:
        cities.append(vert)
        bfs(vert)

print(len(cities)-1)
for i in range(len(cities)-1):
    print('{} {}'.format(cities[i],cities[i+1]))
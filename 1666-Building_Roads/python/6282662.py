from queue import Queue

n, m = map(int, input().split())

num_cities = n + 1
visited = [False] * num_cities
components = []
adjacencies = [[] for _ in range(num_cities)]

for _ in range(m):
    u, v = map(int, input().split())
    adjacencies[u].append(v)
    adjacencies[v].append(u)

queue = Queue()


def bfs(initial):
    queue.put(initial)
    visited[initial] = True

    while not queue.empty():
        node = queue.get()

        for neighbor in adjacencies[node]:
            if not visited[neighbor]:
                queue.put(neighbor)
                visited[neighbor] = True


def find_components():
    for city in range(1, n + 1):
        if not visited[city]:
            components.append(city)
            bfs(city)


find_components()

new_roads = []
first_city = components[0]

for component in components[1:]:
    new_roads.append((first_city, component))
    first_city = component

print(len(new_roads))
for road in new_roads:
    print(*road)
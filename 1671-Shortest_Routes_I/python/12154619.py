import heapq

cities_and_flies = list(map(int, input().split()))


def dijkstra():
    infinite = float('inf')
    dist = [infinite] * (cities_and_flies[0] + 1)
    dist[1] = 0
    heap = [(0, 1)]

    while heap:
        d, node = heapq.heappop(heap)

        if d > dist[node]:
            continue

        for neighbor, cost in graph[node]:
            new_dist = d + cost
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist[1:]


connections = []

for _ in range(cities_and_flies[1]):
    connections.append(list(map(int, input().split())))

graph = [[] for _ in range(cities_and_flies[0] + 1)]
for a, b, c in connections:
    graph[a].append((b, c))


ans = dijkstra()


print(" ".join(list(map(str, ans))))
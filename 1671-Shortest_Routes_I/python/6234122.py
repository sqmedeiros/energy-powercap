import heapq

def shortest_routes(n, m, flights):
    graph = [[] for _ in range(n+1)]
    for a, b, c in flights:
        graph[a].append((b, c))

    distances = [float('inf')] * (n+1)
    distances[1] = 0

    pq = [(0, 1)]

    while pq:
        curr_dist, curr_city = heapq.heappop(pq)

        if curr_dist > distances[curr_city]:
            continue

        for neighbor, dist in graph[curr_city]:
            new_dist = curr_dist + dist

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances[1:]

n, m = map(int, input().split())
flights = []
for _ in range(m):
    a, b, c = map(int, input().split())
    flights.append((a, b, c))

distances = shortest_routes(n, m, flights)
print(*distances)
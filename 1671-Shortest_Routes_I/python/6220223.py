import heapq

def shortest_routes(n, m, connections):
    graph = [[] for _ in range(n + 1)]  

    for a, b, c in connections:
        graph[a].append((b, c)) 

    distances = [float('inf')] * (n + 1)  
    distances[1] = 0  

    heap = [(0, 1)]  
    heapq.heapify(heap)

    while heap:
        dist, city = heapq.heappop(heap)

        if dist > distances[city]:
            continue

        for neighbor, length in graph[city]:
            new_dist = dist + length

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances[1:] 

n, m = map(int, input().split())
connections = []
for _ in range(m):
    a, b, c = map(int, input().split())
    connections.append((a, b, c))

result = shortest_routes(n, m, connections)

print(' '.join(map(str, result)))
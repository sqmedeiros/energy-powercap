import heapq

def dijkstra(graph, start):

    distances = {}
    for node in graph:
      distances[node] = float('inf')
    distances[start] = 0
    pq = [(0, start)]  

    while pq:
        current_dist, current_node = heapq.heappop(pq)  
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


n, m = map(int, input().split())

# hacer grafo en dicc
graph = {}
for i in range(1, n+1):
  graph[i] = []
#print(graph)
for _ in range(m):
  node_1, node_2, weight = map(int, input().split())
  graph[node_1].append((node_2, weight))

#print(graph)

min_distances = dijkstra(graph, 1)
for value in min_distances.values():
  print(f'{value} ',end=' ')
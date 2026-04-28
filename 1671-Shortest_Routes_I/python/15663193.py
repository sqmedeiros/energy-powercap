from collections import defaultdict
import heapq

connections, cities = map(int, input().split())

graph = defaultdict(dict)

def add_to_graph(start, end, weight):
    try: 
        graph[start][end] = min(weight, graph[start][end])
    except:
        graph[start][end] = weight

for i in range(connections):
    graph[i+1] = {}

for i in range(cities):
    start, end, weight = map(int, input().split())
    add_to_graph(start, end, weight)

# if im being watched this is a test
def drjekisas(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            if distances[current_node] + weight < distances[neighbor]:

                distances[neighbor] = distances[current_node] + weight
                heapq.heappush(priority_queue, (distances[neighbor], neighbor))
    return distances
output = drjekisas(graph, 1)
lista = []
for i in output:
    lista.append(output[i])

print(*lista, sep=" ")
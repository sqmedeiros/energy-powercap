from queue import PriorityQueue

n, m = map(int, input().split())

adjacency_list = {}

for _ in range(m):
    a, b = map(int, input().split())

    # Add 'b' to the adjacency list of 'a'
    if a in adjacency_list:
        adjacency_list[a].append(b)
    else:
        adjacency_list[a] = [b]

    # Add 'a' to the adjacency list of 'b'
    if b in adjacency_list:
        adjacency_list[b].append(a)
    else:
        adjacency_list[b] = [a]

def dijkstra(start):
    distances = {node: float('inf') for node in adjacency_list}
    distances[start] = 0
    shortest_path = {}

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        current_distance, current_node = pq.get()

        if current_distance > distances[current_node]:
            continue

        if current_node not in adjacency_list:
            print('IMPOSSIBLE')
            exit()

        for neighbor in adjacency_list[current_node]:
            distance = current_distance + 1

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                pq.put((distance, neighbor))
                shortest_path[neighbor] = current_node

    return distances, shortest_path

start_node = 1
distances, shortest_path = dijkstra(start_node)

if n not in shortest_path:
    print('IMPOSSIBLE')
    exit()

print(distances[n] + 1)

k = n
path = []
while k > 1:
    path.append(shortest_path[k])
    k = shortest_path[k]

for i in reversed(path):
    print(i, end=' ')
print(n)
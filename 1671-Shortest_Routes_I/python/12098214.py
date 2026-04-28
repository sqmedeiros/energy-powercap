import heapq

def dijkstra(graph, start, n):

    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    priority_queue = [(0, start)] 

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def solve_shortest_routes(n, flights):

    graph = [[] for _ in range(n + 1)]
    for a, b, c in flights:
        graph[a].append((b, c))  

    distances = dijkstra(graph, 1, n)

    return distances[1:]  

def main():
    n, m = map(int, input().split())
    flights = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        flights.append((a, b, c))

    shortest_routes = solve_shortest_routes(n, flights)

    print(*shortest_routes)

if __name__ == "__main__":
    main()
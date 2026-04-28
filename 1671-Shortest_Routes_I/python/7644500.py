import heapq

def find_shortest_path(graph, starting_node):
    num_vertices = len(graph)
    shortest_distances = [float('inf')] * num_vertices
    shortest_distances[starting_node] = 0

    priority_queue = [(0, starting_node)]

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        if current_dist > shortest_distances[current_vertex]:
            continue

        for neighbor, edge_weight in graph[current_vertex]:
            dist_to_neighbor = current_dist + edge_weight
            if dist_to_neighbor < shortest_distances[neighbor]:
                shortest_distances[neighbor] = dist_to_neighbor
                heapq.heappush(priority_queue, (dist_to_neighbor, neighbor))

    return shortest_distances

def main():
    num_cities, num_connections = map(int, input().split())
    city_graph = [[] for _ in range(num_cities)]

    for _ in range(num_connections):
        city_from, city_to, distance = map(int, input().split())
        city_graph[city_from - 1].append((city_to - 1, distance))

    starting_city = 0  # Considering Campina Grande
    shortest_distances = find_shortest_path(city_graph, starting_city)

    for distance in shortest_distances:
        print(distance)

if __name__ == "__main__":
    main()
import heapq

INFINITY = float('inf')

def read_directed_weighted_adjacency_list(number_of_nodes: int, number_of_edges: int):
    adjacency_list = [[] for _ in range(number_of_nodes)]

    for _ in range(number_of_edges):
        source_node, target_node, weight = map(int, input().split())
        adjacency_list[source_node - 1].append((target_node - 1, weight))

    return adjacency_list

def main():
    number_of_nodes, number_of_edges = map(int, input().split(' '))
    adjacency_list = read_directed_weighted_adjacency_list(number_of_nodes, number_of_edges)
    source_node = 0

    queue = []
    is_visited = [False for _ in range(number_of_nodes)]
    distance_to_source_node = [INFINITY for _ in range(number_of_nodes)]

    distance_to_source_node[source_node] = 0
    queue.append((distance_to_source_node[source_node], source_node))

    while len(queue) > 0:
        distance, node = heapq.heappop(queue)

        if distance > distance_to_source_node[node]:
            continue
        is_visited[node] = True

        for (adjacent_node, weight) in adjacency_list[node]:
            if is_visited[adjacent_node]:
                continue
            if distance_to_source_node[adjacent_node] > distance_to_source_node[node] + weight:
                distance_to_source_node[adjacent_node] = distance_to_source_node[node] + weight
                heapq.heappush(queue, (distance_to_source_node[adjacent_node], adjacent_node))

    print(*distance_to_source_node)

main()
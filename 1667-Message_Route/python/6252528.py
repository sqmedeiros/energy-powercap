from collections import deque

INFINITY = float('inf')

def read_undirected_adjacency_list(number_of_nodes: int, number_of_edges: int):
    adjacency_list = [[] for _ in range(number_of_nodes)]

    for _ in range(number_of_edges):
        source_node, target_node = (int(node) - 1 for node in input().split(' '))
        adjacency_list[source_node].append(target_node)
        adjacency_list[target_node].append(source_node)

    return adjacency_list

def main():
    number_of_nodes, number_of_edges = map(int, input().split(' '))
    adjacency_list = read_undirected_adjacency_list(number_of_nodes, number_of_edges)

    source_node = 0
    target_node = number_of_nodes - 1

    queue = deque([source_node])
    has_been_reached = [False for _ in range(number_of_nodes)]
    previous_node = [-1 for _ in range(number_of_nodes)]
    distance = [INFINITY for _ in range(number_of_nodes)]

    has_been_reached[source_node] = True
    distance[source_node] = 0

    while len(queue) > 0:
        node = queue.popleft()
        for adjacent_node in adjacency_list[node]:
            if has_been_reached[adjacent_node]:
                continue
            has_been_reached[adjacent_node] = True
            previous_node[adjacent_node] = node
            distance[adjacent_node] = distance[node] + 1
            queue.append(adjacent_node)


    if distance[target_node] == INFINITY:
        print('IMPOSSIBLE')
        return

    number_of_path_nodes = distance[target_node] + 1
    print(number_of_path_nodes)

    path_nodes = [-1 for _ in range(number_of_path_nodes)]
    current_path_node = target_node
    for path_node_index in range(number_of_path_nodes - 1, -1, -1):
        path_nodes[path_node_index] = current_path_node + 1
        current_path_node = previous_node[current_path_node]

    print(*path_nodes)

main()
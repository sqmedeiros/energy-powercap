from collections import deque
from collections import defaultdict

def bfs_shortest_path(graph, start, end):
    visited = set()
    parent = {}  # To reconstruct path
    queue = deque([start])
    visited.add(start)
    parent[start] = None  # Start has no parent

    while queue:
        node = queue.popleft()

        if node == end:
            break  # Found the destination

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                queue.append(neighbor)

    # Reconstruct the path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent.get(current)

    path.reverse()

    if path and path[0] == start:
        return path  # Valid path found
    else:
        return None  # No path exists

def main():
    n, m = map(int, input().split(' '))
    graph = defaultdict(list)

    #print("Enter edges in the format 'u,v' (0-indexed):")
    for _ in range(m):
        u, v = map(int, input().split(' '))
        u -=1
        v -=1
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph

    #start, end = map(int, input("Enter start and end nodes (0-indexed): ").split(','))
    start,end=0, n-1  # Default start and end nodes
    path = bfs_shortest_path(graph, start, end)

    if path:
        print(len(path))#nodes
        #print("Shortest path from node {} to node {} is: {}".format(start, end, path))
        for i in range(len(path)):
            print(path[i]+1, end=' ')  # Print path with 1-indexed nodes
    else:
        print("IMPOSSIBLE")  
if __name__ == "__main__":
    main()
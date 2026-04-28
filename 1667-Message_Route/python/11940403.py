import sys
from collections import deque

def find_shortest_path(n, m, edges):
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    # BFS Initialization
    queue = deque([1])
    parent = [-1] * (n + 1)  # To store path
    visited = [False] * (n + 1)
    visited[1] = True

    # BFS Traversal
    while queue:
        node = queue.popleft()
        if node == n:  # If we reach node n, stop
            break
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)

    # If Maija's computer (n) is unreachable
    if parent[n] == -1:
        print("IMPOSSIBLE")
        return

    # Reconstruct the path from n to 1
    path = []
    current = n
    while current != -1:
        path.append(current)
        current = parent[current]

    # Print the shortest path
    print(len(path))
    print(*reversed(path))

# Input Handling
n, m = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

find_shortest_path(n, m, edges)
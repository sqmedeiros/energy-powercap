from collections import deque

def bfs(src, dest, adj, n):
    queue = deque([src])  # Initialize the queue with the source node
    visited = set()  # Use a set for visited nodes
    visited.add(src)
    parent = [-1] * n  # To store the parent of each node for path reconstruction

    while queue:
        node = queue.popleft()

        # Check if the destination is reached
        if node == dest:
            # Reconstruct path from dest to src using parent array
            path = []
            while node != -1:
                path.append(node + 1)  # Adjusting for 1-based output
                node = parent[node]
            path.reverse()
            return (len(path), path)

        # Explore neighbors
        for neighbor in adj[node]:
            if neighbor not in visited:  # Use set for quick lookup
                visited.add(neighbor)
                parent[neighbor] = node  # Set parent for path reconstruction
                queue.append(neighbor)

    return (-1, [])  # If no path found

# Input and adjacency list setup
n, m = map(int, input().split())
adj = {i: [] for i in range(n)}
for _ in range(m):
    u, v = map(int, input().split())
    adj[u-1].append(v-1)  # Add edge to adjacency list
    adj[v-1].append(u-1)  # Since the graph is undirected

# Define source and destination
src, dest = 0, n - 1
dist, path = bfs(src, dest, adj, n)

# Output result
if dist == -1:
    print("IMPOSSIBLE")
else:
    print(dist)
    print(" ".join(map(str, path)))
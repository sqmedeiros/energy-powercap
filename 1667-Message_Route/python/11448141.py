from collections import defaultdict, deque

class BeingZero:
    def solve(self, edges, n, m):
        # Build graph as adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Sort neighbors for deterministic output
        for node in graph:
            graph[node].sort()

        # BFS initialization
        queue = deque([1])  # Start BFS from node 1
        parent = [-1] * (n + 1)  # To reconstruct path
        visited = [False] * (n + 1)
        visited[1] = True

        # Perform BFS
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    queue.append(neighbor)
                    if neighbor == n:  # Early exit if we reach the target
                        break

        # If no path to n, return IMPOSSIBLE
        if parent[n] == -1:
            return []

        # Reconstruct path from n to 1 using the parent array
        path = []
        current = n
        while current != -1:
            path.append(current)
            current = parent[current]

        path.reverse()  # Reverse to get path from 1 to n
        return path


if __name__ == "__main__":
    n, m = map(int, input().split())  # Number of nodes and edges
    edges = [tuple(map(int, input().split())) for _ in range(m)]  # Input edges
    solver = BeingZero()

    result = solver.solve(edges, n, m)

    if not result:
        print("IMPOSSIBLE")
    else:
        print(len(result))
        print(" ".join(map(str, result)))
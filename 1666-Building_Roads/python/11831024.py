from collections import deque

n, m = map(int, input().split())

# Build adjacency list using a list of lists for speed
land = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    land[a].append(b)
    land[b].append(a)

visited = set()  # use a set for O(1) membership checks
reps = []        # store one representative from each component

def bfs(start):
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in land[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Run BFS from each unvisited node to find all connected components
for i in range(1, n+1):
    if i not in visited:
        reps.append(i)
        bfs(i)

# reps now holds a representative for each connected component
x = len(reps)
print(x-1)  # number of edges to connect all components = (number of components - 1)
for i in range(1, x):
    print(reps[0], reps[i])

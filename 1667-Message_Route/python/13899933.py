from collections import deque

def find_shortest_path(graph, start, end, n):
    visited = [False] * (n + 1)
    prev = [0] * (n + 1)

    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                prev[neighbor] = node
                queue.append(neighbor)

    if not visited[end]:
        print("IMPOSSIBLE")
        return

    path = []
    curr = end
    while curr != 0:
        path.append(curr)
        curr = prev[curr]

    path.reverse()
    print(len(path))
    print(*path)

def main():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    find_shortest_path(graph, start=1, end=n, n=n)

main()
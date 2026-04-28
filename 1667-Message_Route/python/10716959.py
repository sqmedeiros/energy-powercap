from collections import deque, defaultdict


def find_shortest_path():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2

    adj = defaultdict(list)
    for _ in range(m):
        a = int(data[index])
        b = int(data[index + 1])
        adj[a].append(b)
        adj[b].append(a)
        index += 2

    def bfs(start, end):
        visited = set()
        parent = {start: None}
        q = deque([start])
        visited.add(start)

        while q:
            node = q.popleft()
            if node == end:
                break
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    q.append(neighbor)

        if end not in visited:
            return None

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()
        return path

    path = bfs(1, n)

    if path is None:
        print("IMPOSSIBLE")
    else:
        print(len(path))
        print(" ".join(map(str, path)))


if __name__ == "__main__":
    find_shortest_path()
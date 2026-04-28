import sys
from collections import defaultdict

input = sys.stdin.readline


def round_trip():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)

    for start in range(1, n + 1):
        if visited[start]:
            continue
        stack = [(start, -1)]
        while stack:
            u, p = stack.pop()
            if visited[u]:
                continue
            visited[u] = True
            parent[u] = p
            for v in graph[u]:
                if v == p:
                    continue
                if not visited[v]:
                    stack.append((v, u))
                else:
                    # Found a cycle (back edge u-v)
                    path = [v]
                    cur = u
                    while cur != v:
                        path.append(cur)
                        cur = parent[cur]
                    path.append(v)
                    print(len(path))
                    print(*path)
                    return
    print("IMPOSSIBLE")


if __name__ == "__main__":
    round_trip()
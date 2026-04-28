import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)
    cycle_start, cycle_end = -1, -1

    for i in range(1, n + 1):
        if not visited[i] and cycle_start == -1:
            stack = [(i, -1)]

            while stack:
                u, p = stack.pop()

                visited[u] = True
                parent[u] = p

                for v in graph[u]:
                    if v == p:
                        continue

                    if visited[v]:
                        cycle_end = u
                        cycle_start = v
                        break
                    else:
                        stack.append((v, u))

                if cycle_start != -1:
                    break

    if cycle_start == -1:
        print("IMPOSSIBLE")
    else:
        path = [cycle_start]
        curr = cycle_end
        while curr != cycle_start:
            path.append(curr)
            curr = parent[curr]
        path.append(cycle_start)

        path.reverse()

        print(len(path))
        print(*path)

if __name__ == "__main__":
    main()
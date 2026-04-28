from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)


    vis = [False] * n
    parent = [None] * n

    q = deque()
    q.append(0)
    vis[0] = True
    parent[0] = -1

    while q:
        node = q.popleft()
        if node == n - 1:
            break
        for adj in graph[node]:
            if not vis[adj]:
                vis[adj] = True
                parent[adj] = node
                q.append(adj)

    if not vis[n - 1]:
        print("IMPOSSIBLE")
        return

    path = [str(n)]
    i = parent[n - 1]
    while i != -1:
        path.append(str(i + 1))
        i = parent[i]

    print(len(path))
    path = path[::-1]
    print(" ".join(path))

solve()
from collections import deque

def bfs(u, adj, vis, parent):
    q = deque([u])
    vis[u] = True
    parent[u] = u
    while q:
        v = q.popleft()
        for x in adj[v]:
            if not vis[x]:
                vis[x] = True
                parent[x] = v
                q.append(x)

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    vis = [False] * (n + 1)
    parent = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    bfs(1, adj, vis, parent)

    if vis[n]:
        path = []
        x = n
        while parent[x] != x:
            path.append(x)
            x = parent[x]
        path.append(1)
        path.reverse()

        print(len(path))
        print(*path)
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
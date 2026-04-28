from collections import deque

def find_shortest_path():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]

    for i in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)

    vis = [False for _ in range(n)]
    q = deque()
    par = [[None] for _ in range(n)]
    dist = [-1 for _ in range(n)]
    q.append(0)
    vis[0] = True
    dist[0] = 0

    while q:
        x = q.popleft()
        for y in edges[x]:
            if not vis[y]:
                vis[y] = True
                q.append(y)
                dist[y] = dist[x] + 1
                par[y] = x

    if dist[n-1] == -1:
        print("IMPOSSIBLE")
    else:
        print(dist[n-1]+1)
        path = [n]
        end = n - 1
        start = 0
        while end != start:
            x = par[end]
            end = x
            path.append(x+1)

        print(*reversed(path))

if __name__=='__main__':
    find_shortest_path()



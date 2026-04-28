from collections import deque, defaultdict


def bfs(src, des):
    queue = deque()
    dist = defaultdict(int)

    queue.append(src)
    dist[src] = 0
    parent = defaultdict(int)
    parent[src] = src
    while queue:
        curr = queue.popleft()
        for neigh in network[curr]:
            if dist[neigh] == 0:
                dist[neigh] = dist[curr] + 1
                queue.append(neigh)
                parent[neigh] = curr
                if neigh == des:
                    return dist, parent
    return dist, parent


n, m = [int(i) for i in input().split(" ")]
network = defaultdict(list)

for i in range(m):
    u, v = [int(i) for i in input().split(" ")]
    network[u].append(v)
    network[v].append(u)
src, des = 1, n
dist, parent = bfs(src, des)

if des in dist:
    print(dist[des] + 1)
    crawl = des
    path = []
    while crawl != src:
        path.append(crawl)
        crawl = parent[crawl]
    path.append(src)

    print(*path[::-1])


else:
    print("IMPOSSIBLE")
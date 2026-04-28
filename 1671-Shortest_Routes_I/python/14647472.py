import sys
import heapq

def shortestDist(n, m, adj):

    dist = [float("inf")]*(n+1)
    dist[1] = 0

    pq = [(0,1)]

    while pq:

        d, node = heapq.heappop(pq)

        if d > dist[node]:
            continue

        for v,w in adj[node]:
            if dist[node] +  w < dist[v]:
                dist[v] = dist[node] + w
                heapq.heappush(pq, (dist[v], v))

    return dist



def solve():
    input = sys.stdin.readline

    n, m = map(int, input().split())  # number of cities and edges

    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, w = map(int, input().split())
        adj[a].append((b, w))

    res = shortestDist(n,m,adj)
    res = res[1:]
    print(*res)


if __name__ == "__main__":
    solve()

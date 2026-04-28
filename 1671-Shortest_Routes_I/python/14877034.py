from heapq import heappop, heappush

def solve(n, m, AL):
    dist = [float('inf')] * n
    dist[0] = 0
    pq = [(0, 0)]

    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in AL[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heappush(pq, (dist[v], v))

    return dist

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    AL = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a-= 1
        b -= 1
        AL[a].append((b, c))

    res = solve(n, m, AL)
    print(*res)
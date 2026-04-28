from collections import defaultdict
from heapq import heappush, heappop

def solve():
    n, m = list(map(int, input().split()))
    res = [float('inf')] * n
    res[0] = 0
    graph = defaultdict(list)
    for _ in range(m):
        fr, to, dist = list(map(int, input().split()))
        graph[fr].append((to, dist))

    h = [(0, 1)]
    visited = set()
    while h:
        _, node = heappop(h)
        if node in visited:
            continue
        visited.add(node)
        for nei, dist in graph[node]:
            idx = nei - 1
            if res[idx] > res[node-1] + dist:
                res[idx] = res[node-1] + dist
                heappush(h, (res[idx], nei))

    return ' '.join(map(str, res))

print(solve())
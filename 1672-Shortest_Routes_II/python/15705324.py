from copy import deepcopy
from collections import defaultdict,deque
from typing import Optional,List
from math import sqrt,ceil
MOD = 10**9 + 7

import sys
import heapq
input = sys.stdin.readline

n, m, q = map(int, input().split())
if m <= 100000:
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append((b, c))
        adj[b].append((a, c))
    INF = 10**12
    dist = [[INF]*n for _ in range(n)]
    def dijkstra(start):
        d = [INF]*n
        d[start] = 0
        heap = [(0, start)]
        while heap:
            du, u = heapq.heappop(heap)
            if du != d[u]:
                continue
            for v, w in adj[u]:
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    heapq.heappush(heap, (d[v], v))
        dist[start] = d
    for i in range(n):
        dijkstra(i)
    for _ in range(q):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        print(dist[a][b] if dist[a][b] != INF else -1)
else:
    INF = 10**12
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1; v -= 1
        if w < dist[u][v]:
            dist[u][v] = dist[v][u] = w
    for k in range(n):
        dist_k = dist[k]
        for i in range(n):
            dist_i = dist[i] 
            dist_ik = dist_i[k]
            if dist_ik == INF:continue 
            for j in range(n):
                new_dist = dist_ik + dist_k[j]
                if dist_i[j] > new_dist:
                    dist_i[j] = new_dist
    results = []
    for _ in range(q):
        u, v = map(int, input().split())
        res = dist[u-1][v-1]
        results.append(str(res if res != INF else -1))
    sys.stdout.write('\n'.join(results) + '\n')
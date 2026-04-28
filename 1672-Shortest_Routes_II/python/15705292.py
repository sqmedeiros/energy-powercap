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
        adj[b].append((a, c))  # 双向路

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

    # 预处理每个节点的最短路
    for i in range(n):
        dijkstra(i)

    # 查询
    for _ in range(q):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        print(dist[a][b] if dist[a][b] != INF else -1)
else:
    INF = 10**12

    # 初始化邻接矩阵
    dp = [[INF]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1; b -= 1
        if c < dp[a][b]:
            dp[a][b] = c
            dp[b][a] = c  # 双向边

    # Floyd-Warshall
    for k in range(n):
        dpk = dp[k]  # 内存优化，减少 dp[k][j] 访问开销
        for i in range(n):
            dpi = dp[i]
            dik = dpi[k]
            if dik == INF:
                continue
            for j in range(n):
                if dpk[j] != INF and dik + dpk[j] < dpi[j]:
                    dpi[j] = dik + dpk[j]

    # 查询
    for _ in range(q):
        a, b = map(int, input().split())
        a -= 1; b -= 1
        res = dp[a][b]
        print(res if res != INF else -1)
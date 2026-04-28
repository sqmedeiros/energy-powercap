from __future__ import annotations
from array import array

INF = 1 << 59
n, m, q = map(int, input().split())
adj = array("l", [INF] * (n * n))

for i in range(n):
    adj[i + i * n] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if c < adj[a * n + b]:
        adj[a * n + b] = c
        adj[b * n + a] = c

for k in range(n):
    for i in range(n):
        d1 = adj[i * n + k]
        if k == i or d1 == INF:
            continue
        for j in range(i):
            d2 = d1 + adj[k * n + j]
            if d2 < adj[i * n + j]:
                adj[i * n + j] = d2
                adj[j * n + i] = d2

for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    print(adj[a * n + b] if adj[a * n + b] != INF else -1)
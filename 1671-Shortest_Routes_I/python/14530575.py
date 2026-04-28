# import sys
# sys.stdin = open('test.in', 'r')
# sys.stdout = open('test.out', 'w+')

import heapq
from collections import defaultdict
BIG = int(1e18)
n, m = map(int, input().split())
distance = [BIG]*n
distance[0] = 0
adj = defaultdict(list)
q = [(0,0)]
processed = [False]*n

for _ in range(m):
    a,b,w = map(int, input().split())
    # flight a -> b
    adj[a-1].append((w,b-1))

while q:
    _, curr = heapq.heappop(q)
    if processed[curr]:
        continue

    processed[curr] = True
    for nei in adj[curr]:
        w, v = nei
        distance[v] = min(distance[v], distance[curr] + w)
        heapq.heappush(q, (distance[v], v))

print(*distance)
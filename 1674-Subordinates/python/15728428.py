n = int(input())

par = [0, -1] + list(map(int, input().split()))

digraph = {i:[] for i in range(1, n+1)}

for i in range(2, n+1):
    digraph[par[i]].append(i)

subs = [0] * (n+1)

dist = [0] * (n+1)

from collections import deque

queue = deque()

queue.append((1, 0))

visited = [0] * (n+1)
visited[1] = 1

while queue:
    p, d = queue.pop()
    for q in digraph[p]:
        if visited[q] == 0:
            dist[q] = d + 1
            queue.append((q, d+1))

dist_ind = [(dist[i], i) for i in range(1, n+1)]

dist_ind = sorted(dist_ind, reverse=True)

for d, p in dist_ind:
    for s in digraph[p]:
        subs[p] += subs[s] + 1

print(' '.join(map(str, subs[1:])))
from collections import defaultdict
import sys
from collections import deque
sys.setrecursionlimit(10 ** 5)
n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    edge = tuple(map(int, input().split()))
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

visited = set()
p = [None] * (n + 1)
cycle = deque()
start = None
end = None
def dfs(v, prev=-1):
    if v in visited:
        global start
        global end
        start = v
        end = prev
        raise SystemExit
    visited.add(v)
    p[v] = prev
    for u in graph[v]:
        if u != prev:
            dfs(u, v)


try:
    for vertex in range(1, n + 1):
        if vertex not in visited:
            dfs(vertex)
    print('IMPOSSIBLE')
except SystemExit:
    curr = end
    cycle.appendleft(start)
    while curr != start:
        cycle.appendleft(curr)
        curr = p[curr]
    cycle.appendleft(start)
    print(len(cycle))
    print(*cycle)







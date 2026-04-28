import sys
from typing import List, Set
import math
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right

MOD = (10 ** 9) + 7

def message_route(n: int, m: int, edges: List[List[int]]) -> List[int]:
    g = defaultdict(list)
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)


    # do bfs
    q = deque([1])
    parent = defaultdict(lambda: -1)
    dist = defaultdict(lambda: float('inf'))
    dist[1] = 1
    while q:
        i = q.popleft()

        # visit
        if i == n:
            # found
            break

        for neigh in g[i]:
            if dist[neigh] != float('inf'): # already visited
                continue

            parent[neigh] = i
            dist[neigh] = dist[i] + 1

            q.append(neigh) # explore neigh's descendants next

    if dist[n] == float('inf'):
        return [] # not found

    path = []
    walk = n
    while walk != -1:
        path.append(walk)
        walk = parent[walk]

    # print('path dist', path, dist[n])

    return list(reversed(path))

if __name__ == "__main__":
    stdin = sys.stdin
    stdout = sys.stdout

    n, m = list(map(int, stdin.readline().split()))
    edges = []
    for _ in range(m):
        edges.append(list(map(int, stdin.readline().split())))

    path = message_route(n, m, edges)

    if len(path) == 0:
        stdout.write("IMPOSSIBLE" + '\n')
    else:
        stdout.write(str(len(path)) + '\n')
        stdout.write(' '.join(list(map(str, path))) + '\n')

    stdout.flush()
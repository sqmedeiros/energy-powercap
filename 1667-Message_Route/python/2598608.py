import sys
from os import path

sys.setrecursionlimit(10 ** 6)

if path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')


def BFS(v):
    q = [v]
    visited[v] = True
    dis[v] = 0
    while len(q) > 0:
        curr = q[0]
        q.pop(0)
        for x in range(len(g[curr])):
            child = g[curr][x]
            if not visited[child]:
                q.append(child)
                dis[child] = dis[curr] + 1
                visited[child] = True
                p[child] = curr
                if visited[n]:
                    return True
    return False


n, m = map(int, sys.stdin.readline().rstrip().split())
a = []
g = [[] * 1 for i in range(n + 1)]
for x in range(m):
    b = list(map(int, sys.stdin.readline().rstrip().split()))
    a.append(b)

for x in range(m):
    g[a[x][0]].append(a[x][1])
    g[a[x][1]].append(a[x][0])
visited = [False] * (n + 1)
dis = [0] * (n + 1)
p = [-1] * (n + 1)
visited[0] = True
t = BFS(1)
if not t:
    print("IMPOSSIBLE")
else:
    path = [n]
    c = n
    while p[c] != -1:
        path.append(p[c])
        c = p[c]
    print(dis[n]+1)
    for x in range(len(path) - 1, -1, -1):
        print(path[x], end=" ")

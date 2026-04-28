# author: ankan2526

import sys,math,heapq,bisect,random,itertools
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

ints = lambda : list(map(int,input().split()))
def gprint(ans=''):global t;print(f"Case #{t+1}:",ans)
p = 10**9+7
inf = 10**20+7
adj = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = "abcdefghijklmnopqrstuvwxyz"
ANS = []



'''
'''


def dfs(node, par):
    visited[node] = 1
    for i in graph[node]:
        if i == par:
            continue
        if visited[i] == 1:
            return i, node
        else:
            x = dfs(i, node)
            if x:
                return x

def find_path(node, target, par):
    if node == target:
        return [node]

    if visited[node] == 1:
        return
    visited[node] = 1

    for i in graph[node]:
        if i == par:
            continue
        x = find_path(i, target, node)
        if x:
            x.append(node)
            return x



n, m = ints()

graph = [[] for i in range(n+1)]

for i in range(m):
    x, y = ints()
    graph[x].append(y)
    graph[y].append(x)


## Find Cycle in a Graph

# try:
#     visited = [0] * (n+1)
#     x, y = dfs(1, 0)
#     visited = [0] * (n+1)
#     path = find_path(x, y, y) + [y]
#     print(len(path))
#     print(*path)
# except:
#     print("IMPOSSIBLE")

visited = [0] * (n+1)

for i in range(1, n+1):
    if visited[i] == 0:
        a = dfs(i, 0)
        if a:
            x, y = a
            visited = [0] * (n+1)
            path = find_path(x, y, y) + [y]
            print(len(path))
            print(*path)
            quit()

print("IMPOSSIBLE")
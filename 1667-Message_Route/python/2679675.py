from collections import defaultdict

def bfs(v):
    q.append(v)
    visited[v] = True
    while q:
        v = q.pop(0)
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                parent[i] = v

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = {i+1:False for i in range(n)}
path = []
q = []
parent = {i:-1 for i in range(1,n+1)}
parent[1] = 1
bfs(1)
x = n
# print(parent)
flag = True
while x != 1:   
    if x == -1:
        flag = False
        break
    path.append(x)
    x = parent[x]
path.append(1)
if flag:
    print(len(path))
    print(*path[::-1])
else:
    print("IMPOSSIBLE")
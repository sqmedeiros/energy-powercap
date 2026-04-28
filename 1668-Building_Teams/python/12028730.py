from collections import deque

n, m = map(int, input().split())
graph = [[] for i in range (n + 1)]
for i in range (m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

colors = [-1 for i in range (n + 1)]
def BFS(start):
    colors[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if colors[v] == -1:
                colors[v] = 1 - colors[u]
                q.append(v)
            elif colors[v] == colors[u]:
                return False 

    return True 
ans = True
for i in range (1, n + 1):
    if colors[i] == -1:
        cur_ans = BFS(i)
        if cur_ans == False:
            ans = False 
            break

if ans:
    for i in range (1, n + 1):
        print(colors[i] + 1, end = " ")
else:
    print("IMPOSSIBLE")
from collections import deque
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, e = map(int, input().split())
adj = [[] for i in range(n+1)]
vis = [False for i in range(n+1)]
parent = [-1 for i in range(n+1)]

# def backtrack():
#     ans = [n]
#     i = n
#     while(parent[i]!=-1):
#         ans.append(parent[i])
#         i = parent[i]
#     return ans[::-1]

def bfs(node):
    vis[node] = True
    q = deque()
    q.append(node)
    parent[node] = 1
    while(q):
        a = q.popleft()
        color = parent[a]
        for child in adj[a]:
            if(vis[child] and parent[child] == parent[a]):
                return False
            if(not vis[child]):
                parent[child] = a
                q.append(child)
                vis[child] = True
                if(parent[a] == 1):
                    parent[child] = 2
                else:
                    parent[child] = 1
    return True


for i in range(e):
    a, b = map(int, input().split())
    adj[b].append(a)
    adj[a].append(b)

for i in range(1, n+1):
    if(not vis[i]):
        flag = bfs(i)
        if(not flag):
            print("IMPOSSIBLE")
            exit()
print(*parent[1:])

# if(bfs(1)):
#     print(*parent)
# else:
#     print("IMPOSSIBLE")


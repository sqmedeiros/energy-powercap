import sys
from collections import *
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
I = lambda: map(int, input().split())

n,m= I()
g=defaultdict(list)
for _ in range(m):
    a,b= I()
    g[a].append(b)
    g[b].append(a)

parent=[-1]*(n+1)
vis = [False]*(n+1)

q=deque([1])
vis[1]=True
while q:
    u=q.popleft()
    for v in g[u]:
        if not vis[v]:
            vis[v]=True
            parent[v]=u
            q.append(v)
if parent[n]==-1:
    print("IMPOSSIBLE")
    sys.exit()

res=[]
while n!=-1:
    res.append(n)
    n=parent[n]
print(len(res))
print(*res[::-1])


# ####################################################################################
# # Please consider trying a few more times before referring to this code. 
# # Code might be incorrect - TLE / Wrong Answer (especially filenames with _1 , _2)
# # Pedagogical > Pythonic
# ####################################################################################


# from collections import defaultdict, deque
# I = lambda : map(int, input().split())

# n, m = I()
# adj = defaultdict(list)

# for _ in range(m):
#     a, b = I()
#     adj[a].append(b)
#     adj[b].append(a)

# # bfs
# vis = [False] * (n + 1)
# q = deque([1])
# dist = {}
# dist[1] = (0, 0)
# vis[1] = True

# # print(adj)

# while q:
#     # print(q)
#     u = q.popleft()
#     d, _ = dist[u]
#     for v in adj[u]:
#         if not vis[v]:
#             vis[v] = True
#             dist[v] = (d + 1, u)
#             q.append(v)

#         if v == n: 
#             print(dist[v][0] + 1)
#             path = [v]
#             while True:
#                 path.append(dist[v][1])
#                 v = dist[v][1]
#                 if v == 1: break
#             path = path[::-1]
#             print(*path)
#             q = []
#             exit()


# print("IMPOSSIBLE")


# # I once again ask you to try a few more times before referring here
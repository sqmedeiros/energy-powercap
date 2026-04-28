def bfs(s, adj_mat):
    nodes, vis[s] = {s}, 1
    while nodes:
        node = nodes.pop()
        for adj in adj_mat.get(node, []):
            if not vis[adj]:
                vis[adj] = 1
                nodes.add(adj)

# from tkinter import Tk
# inpt=iter(Tk().clipboard_get().split('\n'))
# N,M=map(int,next(inpt).split())

N, M = map(int, input().split())

adj_mat, vis, rep = {}, [0] * N, []
for _ in range(M):
    # i, j = map(int, next(inpt).split())
    i, j = map(int, input().split())
    i, j = i - 1, j - 1
    lst = adj_mat.setdefault(i, [])
    lst.append(j)
    lst = adj_mat.setdefault(j, [])
    lst.append(i)

for i in range(N):
    if not vis[i]:
        rep.append(i)
        bfs(i, adj_mat)

print(len(rep) - 1)
for i in range(len(rep)-1):
    print(rep[i]+1, rep[i+1]+1)
'''
10 10
2 5
5 6
1 4
6 8
2 6
3 6
1 10
8 9
2 3
5 8
'''
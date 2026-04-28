import sys
sys.setrecursionlimit(200000)

# 0. read input
n, m = input().split()
n, m = int(n), int(m)
# n = number of pupils
# m = friendships

# 1. create adjacency list
adj = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b = input().split()
    a, b = int(a), int(b)
    adj[a].append(b)
    adj[b].append(a)

# 2. dfs
color = [0] * (n+1)
bipartite = True


def color_em(cur, cc):
    global color
    global bipartite

    color[cur] = cc

    nc = 1
    if cc == 1:
        nc = 2

    for n in adj[cur]:
        if color[n] == 0:
            color_em(n, nc)
        if color[n] == cc:
            bipartite = False
            print("IMPOSSIBLE")
            exit()


for i in range(1, n+1):
    if color[i] == 0:
        color_em(i, 1)

print(' '.join([str(c) for c in color[1:]]))
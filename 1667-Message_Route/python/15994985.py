from collections import deque

n, m = map(int, input().split())
adj = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

d = [-1 for i in range(n + 1)]
trace = [-1 for i in range(n + 1)]
def bfs(start_node, finish_node):
    d[start_node] = 0
    q = deque()
    q.append(start_node)
    reached_finish_node = False
    while len(q) > 0:
        u = q[0]
        q.popleft()
        if u == finish_node:
            reached_finish_node = True
            rev_nodes = [finish_node]
            while trace[u] != -1:
                u = trace[u]
                rev_nodes.append(u)
            nodes = list(reversed(rev_nodes))
            print(d[finish_node] + 1)
            for i in range(len(nodes)):
                print("{} ".format(nodes[i]), end = "")
            print("")
            break

        for i in range(len(adj[u])):
            v = adj[u][i]
            if d[v] == -1:
                d[v] = d[u] + 1
                trace[v] = u
                q.append(v)

    if reached_finish_node == False:
        print("IMPOSSIBLE")

bfs(1, n)



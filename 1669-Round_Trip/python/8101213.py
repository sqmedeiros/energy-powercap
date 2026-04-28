import sys
sys.setrecursionlimit(1_000_000)
nodes_cnt, edges_cnt = map(int, sys.stdin.readline().strip().split())
unweighted_graph = [[] for _ in range(nodes_cnt)]

for _ in range(edges_cnt):
    a, b = map(int, sys.stdin.readline().strip().split())
    a -= 1
    b -= 1
    unweighted_graph[a].append(b)
    unweighted_graph[b].append(a)

parent_of = [None] * nodes_cnt
dfs_status = [0] * nodes_cnt
def find_cycle(node: int) -> int or None:
    dfs_status[node] = -1
    for neighbor in unweighted_graph[node]:
        assert dfs_status[neighbor] != 1
        if parent_of[node] == neighbor:
            continue
        if dfs_status[neighbor] == -1:
            cycle = [node]
            while parent_of[cycle[-1]] != neighbor:
                cycle.append(parent_of[cycle[-1]])
            cycle.append(neighbor)
            cycle.append(cycle[0])
            print(len(cycle))
            print(*[c + 1 for c in cycle])
            exit()
        elif dfs_status[neighbor] == 0:
            parent_of[neighbor] = node
            find_cycle(neighbor)
    dfs_status[node] = 1

for node in range(nodes_cnt):
    if dfs_status[node] == 0:
        find_cycle(node)
print('IMPOSSIBLE')
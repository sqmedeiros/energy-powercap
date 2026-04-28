# Store the graph as an adjacency list.
n, m = map(int, input().split())
adj_list = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a-1].append(b-1)
    adj_list[b-1].append(a-1)


# Run a DFS to find the cycle endpoints. Note that we only mark nodes as
# processed once we remove them from the stack so that the latest edge we find
# into them before processing them is the one we derive the parent from.
parent = [None] * n
processed = [False] * n
cycle_endpoints = None
for start_node in range(n):
    if parent[start_node] is not None:
        continue
    if cycle_endpoints:
        break
    parent[start_node] = -1
    dfs_stack = [start_node]
    while dfs_stack:
        node = dfs_stack.pop()
        if processed[node]:
            continue
        processed[node] = True
        for other in adj_list[node]:
            if other == parent[node]:
                continue
            if processed[other]:
                cycle_endpoints = (other, node)
                break
            else:
                parent[other] = node
                dfs_stack.append(other)
        if cycle_endpoints:
            break


# If a cycle has been found, backtrack through the parents to recover all the
# nodes in it.
if cycle_endpoints:
    cycle = [cycle_endpoints[0]]
    node = cycle_endpoints[1]
    while node != cycle_endpoints[0]:
        cycle.append(node)
        node = parent[node]
    else:
        cycle.append(cycle_endpoints[0])
    print(len(cycle))
    print(' '.join(map(lambda x: str(x+1), cycle)))
else:
    print("IMPOSSIBLE")
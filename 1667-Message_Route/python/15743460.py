n, m = map(int, input().split())

adjacency_lists = [[] for _ in range(n+1)]
parent = [-1 for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    adjacency_lists[a].append(b)
    adjacency_lists[b].append(a)

current_q = [1]
visited[1] = True          # ✅ FIX 1
found = False

while current_q:
    next_q = []
    for item in current_q:
        if item == n:
            found = True
            break

        for nei in adjacency_lists[item]:
            if not visited[nei]:
                visited[nei] = True
                parent[nei] = item
                next_q.append(nei)

    if found:              # ✅ FIX 2
        break

    current_q = next_q

if not found:
    print("IMPOSSIBLE")
else:
    # reconstruct path
    path = []
    cur = n
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    print(len(path))       # ✅ FIX 3 (correct distance)
    print(*path)
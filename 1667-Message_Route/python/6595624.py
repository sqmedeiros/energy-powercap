n, m = map(int, input().split())
adj_list = [[] for _ in range(n+1)]

for _ in range(0, m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited = [False] * (n+1)
parent = [-1] * (n+1)

source = 1
destination = n

queue = [(0, source)]
visited[source] = True
ans = -1
while len(queue) > 0:
    level, node = queue.pop(0)
    for e in adj_list[node]:
        if not visited[e]:
            visited[e] = True
            queue.append((level+1, e))
            parent[e] = node
            # Só roda até encontrar o nó de destino
            if e == destination:
                ans = level+2 # d+1 (nível) + 1 (nó inicial)
                break

if ans == -1:
    print("IMPOSSIBLE")
else:
    print(ans)
    route = []
    current_node = destination
    while current_node != -1:
        route.append(current_node)
        current_node = parent[current_node]
    for x in route[::-1]:
        print(x, '', end='')
    print()

import sys
from collections import defaultdict, deque

read = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, read().split(' '))

adj = defaultdict(list)
for _ in range(m):
    a, b = map(int, read().split(' '))

    adj[a].append(b)
    adj[b].append(a)

visited = [None] * n
visited[0] = 1
cost = 0

queue = deque([1])
while queue:
    node = queue.pop()

    for neigh in adj[node]:
        if visited[neigh - 1] is None:
            if node == n:
                visited[neigh - 1] = node
                queue.clear()
                break

            visited[neigh - 1] = node
            queue.appendleft(neigh)

if visited[n - 1] is not None:
    path = [n]
    current_node = n
    while visited[current_node - 1] != current_node:
        current_node = visited[current_node - 1]
        path.append(current_node)

    path.reverse()
    write(f"{len(path)}\n")
    write(' '.join(map(str, path)))
else:
    write("IMPOSSIBLE")
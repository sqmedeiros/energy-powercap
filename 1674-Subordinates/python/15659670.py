n = int(input())
parents = list(map(int, input().split()))

adj = [[] for _ in range(n + 1)]
for i in range(n - 1):
    adj[parents[i]].append(i + 2)

size = [0] * (n + 1)
stack = [(1, False)]

while stack:
    node, visited = stack.pop()
    if visited:
        for child in adj[node]:
            size[node] += size[child] + 1
    else:
        stack.append((node, True))
        for child in adj[node]:
            stack.append((child, False))

print(*size[1:])
n = int(input())
arr = [int(c) for c in input().split()]

# Create adjacency list
adj = {i: [] for i in range(1, n+1)}
v = 2
for parent in arr:
    adj[parent].append(v)
    v += 1

res = [0] * n
stack = [(1, False)]  # (node, visited flag)
subtree_sizes = [0] * (n + 1)  # Subtree size for each node

while stack:
    node, visited = stack.pop()
    if visited:
        # All children are processed; calculate subtree size
        size = 0
        for child in adj[node]:
            size += subtree_sizes[child]
        subtree_sizes[node] = size + 1
        res[node - 1] = size
    else:
        # First time visiting the node
        stack.append((node, True))  # Push the node back with visited=True
        for child in adj[node]:
            stack.append((child, False))  # Push all children with visited=False

print(*res)
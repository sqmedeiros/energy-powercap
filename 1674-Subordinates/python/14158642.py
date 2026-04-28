n = int(input())
parent = list(map(int, input().split()))

children = [[] for _ in range(n + 1)]
for i, p in enumerate(parent, start=2):
    children[p].append(i)

ans = [0] * (n + 1)
stack = [(1, 0)]
subtree_sizes = [0] * (n + 1)

while stack:
    node, state = stack.pop()
    if state == 0:
        stack.append((node, 1))
        for child in children[node]:
            stack.append((child, 0))
    else:
        total = sum(subtree_sizes[child] for child in children[node])
        ans[node] = total
        subtree_sizes[node] = total + 1

print(" ".join(map(str, ans[1:])))
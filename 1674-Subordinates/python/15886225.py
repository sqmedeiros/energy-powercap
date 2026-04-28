import sys

input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))

adj = [[] for _ in range(N)]
for i, x in enumerate(line):
    u = i+1
    v = x-1
    adj[u].append(v)
    adj[v].append(u)

size = [1] * N
def dfs_subtree_size(root):
    stack = [(root, None, 0)] # (node, parent, status)
    while stack:
        node, par, status = stack.pop()
        if status == 0:
            # mark it as started processing
            stack.append((node, par, 1))
            for c in adj[node]:
                if c == par:
                    continue
                stack.append((c, node, 0))
        else:
            # we have finished processing all of our children
            for c in adj[node]:
                if c == par:
                    continue
                size[node] += size[c]

dfs_subtree_size(0)

for i in range(N):
    size[i] -= 1

print(*size)
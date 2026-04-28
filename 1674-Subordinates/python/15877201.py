import sys

input = sys.stdin.readline

N = int(input())

line = list(map(int, input().split()))

adj = [[] for _ in range(N)]

for i in range(1, N):
    p_i = line[i-1]-1
    adj[p_i].append(i)
    adj[i].append(p_i)

size = [1] * N

stack = [(0, None, 0)] # (node, parent, status)
while stack:
    node, par, status = stack.pop()
    if status == 1:
        # we've calculated all of its children
        for c in adj[node]:
            if c == par:
                continue
            size[node] += size[c]
    else:
        stack.append((node, par, 1)) # set status to started
        for c in adj[node]:
            if c == par:
                continue
            stack.append((c, node, 0))

for i in range(N):
    size[i] -= 1

print(*size)
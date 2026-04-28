import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
for i, p in enumerate(map(int, input().split()), start=2):
    adj[p].append(i)

res = [0] * (n + 1)
stack = [(1, False)]

while stack:
    u, backtrack = stack.pop()
    if backtrack:
        total = 0
        for v in adj[u]:
            total += res[v] + 1
        res[u] = total
    else:
        stack.append((u, True))
        for v in adj[u]:
            stack.append((v, False))

print(*res[1:])
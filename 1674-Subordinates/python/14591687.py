#Given the structure of a company, your task is to calculate for each employee the number of their subordinates.


n = int(input())
data = list(map(int, input().split()))

# build children lists (1-indexed)
g = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    p = data[i - 2]
    g[p].append(i)

subtree = [0] * (n + 1)
res = [0] * (n + 1)

# DFS
stack = [(1, 0)]
while stack:
    u, st = stack.pop()
    if st == 0:
        stack.append((u, 1))
        for v in g[u]:
            stack.append((v, 0))
    else:
        s = 1
        for v in g[u]:
            s += subtree[v]
        subtree[u] = s
        res[u] = s - 1

for i in range(1, n + 1):
    print(res[i])
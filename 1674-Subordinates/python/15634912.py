import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
bosses = list(map(int, sys.stdin.readline().split()))

# Build tree
tree = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    tree[bosses[i - 2]].append(i)

sub = [0] * (n + 1)

def dfs(u):
    sub[u] = 1  # count itself
    for v in tree[u]:
        dfs(v)
        sub[u] += sub[v]

dfs(1)

# Print number of subordinates
print(" ".join(str(sub[i] - 1) for i in range(1, n + 1)))
import sys
sys.setrecursionlimit(10**7)

n = int(input())
bosses = list(map(int, input().split()))

# Each employee will have a list of children
children = [[] for _ in range(n+1)]

# Build the tree
for emp in range(2, n+1):
    boss = bosses[emp-2]
    children[boss].append(emp)

sub = [0] * (n+1)

def dfs(u):
    total = 0
    for v in children[u]:
        dfs(v)
        total += 1 + sub[v]   # child itself + child’s subordinates
    sub[u] = total

dfs(1)
print(*sub[1:])
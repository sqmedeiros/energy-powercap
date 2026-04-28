import sys

sys.setrecursionlimit(200006)  # set recursion limit


def dfs(x):  # x is the current node
 ans = 0  # stores the number of subordinates
 for e in edges[x]:
  if e != fa[x - 1]:
   ans += dfs(e)
 sub[x - 1] = ans  # 0-index is more convenient for printing
 return ans + 1  # add the node x itself


N = int(input())
edges = [[] for _ in range(N + 1)]  # create empty adjacency list
sub = [0 for _ in range(N)]  # the number of subordinates
fa = [1] + list(
 map(int, input().split())
)  # the parent of each node, set the parent of node 1 to itself
for ind, f in enumerate(fa):
 edges[f].append(ind + 1)  # add edges to the adjacency list
dfs(1)
for i in sub:
 print(i, end=" ")
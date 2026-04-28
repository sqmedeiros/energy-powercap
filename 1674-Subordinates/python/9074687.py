from collections import defaultdict
import sys
sys.setrecursionlimit(10000000)
n = int(input())
edges = map(int , input().split(' '))

graph = defaultdict(list)

class Solve:
    def __init__(self,graph) -> None:
        self.graph = graph
    def solve(self):
        self.ans = [0] * n
        self.dfs(graph , 1)
        print(*self.ans)

    def dfs(self, graph , start):
        for nei in graph[start]:
            self.ans[start - 1] += 1
            self.dfs(graph , nei)
            self.ans[start - 1] += self.ans[nei - 1]

for indx, v in enumerate(edges , 2):
    graph[v].append(indx)

Solve(graph).solve()
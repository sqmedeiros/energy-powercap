from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)


class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, u, visited):
        stack = list()
        stack.append(u)
        visited[u] = True
        while stack:
            u = stack.pop()
            for v in self.adj[u]:
                if not visited[v]:
                    stack.append(v)
                    visited[v] = True

    def make_connected(self):
        components = []
        visited = [False] * (n + 1)
        for u in range(1, n + 1):
            if not visited[u]:
                components.append(u)
                self.dfs(u, visited)
        count_edges = len(components) - 1
        print(count_edges)
        for i in range(count_edges):
            print(components[i], components[i + 1])


n, m = map(int, input().split())
g = Graph(n)
for _ in range(m):
    u, v = map(int, input().split())
    g.add_edge(u, v)
g.make_connected()
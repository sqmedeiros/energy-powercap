import sys
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parent[py] = px
            return True
        return False

def buildroad(n, m, edges):
    dsu = DSU(n)
    for u, v in edges:
        dsu.union(u, v)

    reps = []
    for i in range(1, n + 1):
        if dsu.find(i) == i:
            reps.append(i)

    print(len(reps) - 1)
    for i in range(1, len(reps)):
        print(reps[i - 1], reps[i])

# Input
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

buildroad(n, m, edges)
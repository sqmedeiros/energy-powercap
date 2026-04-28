import sys


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] += 1
            return True
        return False


n, m = map(int, sys.stdin.readline().split())
uf = UnionFind(n)


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    uf.union(a, b)


components = set()
for i in range(1, n + 1):
    components.add(uf.find(i))


components = list(components)
num_new_roads = len(components) - 1
new_roads = [(components[i], components[i+1]) for i in range(num_new_roads)]


print(num_new_roads)
for road in new_roads:
    print(*road)
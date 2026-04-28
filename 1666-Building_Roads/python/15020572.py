class DisjointSet:
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def findRoot(self, x):
        while x != self.root[x]:
            self.root[x] = self.findRoot(self.root[x])
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX, rootY = self.findRoot(x), self.findRoot(y)
        if rootX == rootY:
            return False
        self.root[rootY] = rootX
        return True

n, m = map(int, input().split())
disjointSet = DisjointSet(n)
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    disjointSet.union(u, v)

roots = []
for i in range(n):
    if i == disjointSet.findRoot(i):
        roots.append(i)

print(len(roots)-1)
for i in roots[1:]:
    print(roots[0]+1, i+1)
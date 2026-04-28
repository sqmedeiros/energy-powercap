class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


n, m = map(int, input().split())
dsu = DisjointSetUnion(n)
for _ in range(m):
    u, v = map(int, input().split())
    dsu.union(u - 1, v - 1)
root = dsu.find(0)
seen = {root}
l = []
for i in range(n):
    root_i = dsu.find(i)
    if root_i not in seen:
        seen.add(root_i)
        l.append((i + 1, root + 1))

print(len(l))
for e in l:
    print(*e)
from collections import defaultdict


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            if self.rank[pu] > self.rank[pv]:
                self.parent[pv] = pu
            elif self.rank[pu] < self.rank[pv]:
                self.parent[pu] = pv
            else:
                self.parent[pv] = pu
                self.rank[pu] += 1
            return True
        return False

n, m = map(int, input().split())

ds = DisjointSet(n)

for _ in range(m):
    u, v = map(int, input().split())
    ds.union(u - 1, v - 1)

components = defaultdict(list)
for i in range(n):
    root = ds.find(i)
    components[root].append(i)

needed_edges = []
components_list = list(components.keys())

for i in range(1, len(components_list)):
    u = components[components_list[i - 1]][0]
    v = components[components_list[i]][0]
    needed_edges.append((u + 1, v + 1))  
print(len(needed_edges))
for u, v in needed_edges:
    print(u, v)
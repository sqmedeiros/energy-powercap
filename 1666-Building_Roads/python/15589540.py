class UnionFind:
    def __init__(self, n):
        self.parent = [0]*n
        for i in range(n):
            self.parent[i] = i
        self.rank = [0]*n
        self.count = n        

    def find(self, i):  # finds the parent with path compression
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty: # if different roots
            if self.rank[rootx] > self.rank[rooty]: # x has higher rank
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1
    def getCount(self):
        return self.count 

n, m = map(int, input().split())
uf = UnionFind(n) 

for i in range(m):
    a, b = map(int, input().split())
    uf.union(a-1,b-1)
print(uf.getCount()-1)
# print minimum roads needed to connect all components eg : 2 3
# gather all the nodes whose parent is itself
components = []
for i in range(n):
    if uf.find(i) == i:
        components.append(i+1)
# print the roads needed to connect all components
for i in range(1, len(components)):
    print(components[0], components[i])



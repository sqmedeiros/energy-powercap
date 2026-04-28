# union-find
# find(x) -> gives the component for x (some particular vertex in that component)
# union(x,y) -> combine the components for x and y

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.UF = [i for i in range(n)]
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        self.UF[px] = py
    def find(self, x):
        if self.UF[x] == x:
            return x
        self.UF[x] = self.find(self.UF[x])
        return self.UF[x]

n,m = [int(x) for x in input().split()]
UF = UnionFind(n)
for _ in range(m):
    a,b = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    UF.union(a,b)

ANS = []
for i in range(n):
    if UF.find(i) != UF.find(0):
        ANS.append((0,i))
        UF.union(i, 0)
print(len(ANS))
for (a,b) in ANS:
    print(a+1, b+1)
import sys
import collections

sys.setrecursionlimit(200000)

def main():
    n,m = map(int,input().split())
    graph = collections.defaultdict(list)
    dsu = DSU(n)
    for _ in range(m):
        u,v = map(int,input().split())
        dsu.union(u,v)

    parents = []
    for i in range(1,n+1):
        if dsu.parent[i] == i:
            parents.append(i)
    print(len(parents)-1)
    for i in range(len(parents)-1):
        print(parents[i],parents[i+1])
class DSU:

    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]

    def find(self,x):
        if x == self.parent[x]:return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rx = self.find(x)
        ry = self.find(y)

        if rx==ry:return

        if self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[rx] = ry
            self.rank[ry] += 1
if __name__ == "__main__":
    main()
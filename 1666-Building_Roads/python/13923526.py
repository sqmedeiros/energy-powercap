class Disjoint_set:
    def __init__(self, n):
        self.rank = [0]*(n+1)
        self.parent = [i for i in range(n+1)]
        self.size = [1]*(n+1)

    def findUPar(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def UnionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

        return True

def main():
    N, M = map(int, input().split())
    dsu = Disjoint_set(N)
    ans = []

    for _ in range(M):
        a, b = map(int, input().split())
        dsu.UnionBySize(a, b)

    for i in range(1, N):
        if dsu.UnionBySize(i, i + 1):
            ans.append((i, i + 1))

    print(len(ans))
    for u, v in ans:
        print(u, v)

if __name__ == "__main__":
    main()
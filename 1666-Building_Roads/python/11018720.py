class Disjointset:
    def __init__(self,n):
        self.n=n
        self.rank=[0]*(n+1)
        self.parent=[i for i in range(n+1)]
    def findupar(self,node):
        if self.parent[node]==node:
            return node
        self.parent[node]=self.findupar(self.parent[node])
        return self.parent[node]
    def union_by_rank(self,u,v):
        u_par=self.findupar(u)
        v_par=self.findupar(v)
        if u_par==v_par:
            return
        if self.rank[u_par]>self.rank[v_par]:
            self.parent[v_par]=u_par
        elif self.rank[u_par]<self.rank[v_par]:
            self.parent[u_par]=v_par
        else:
            self.parent[v_par]=u_par
            self.rank[u_par]+=1







n,m=map(int,input().split())
adj=[[] for i in range(n)]

ds=Disjointset(n)
for i in range(m):
    u,v=map(int,input().split())
    ds.union_by_rank(u,v)
# print(ds.parent)
# print(ds.rank)
cnt=0
nodes=[]
for i in range(1,n+1):
    if ds.parent[i]==i:
        cnt+=1
        nodes.append(i)
edges=[]
print(cnt-1)
for i in range(1,len(nodes)):
    print(nodes[0],nodes[i])

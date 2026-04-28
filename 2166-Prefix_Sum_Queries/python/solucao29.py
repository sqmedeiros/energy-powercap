import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
sint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
###############################################
##Segtree for range update instead of range addition
def segfunc(x,y):
    return (x[0]+y[0],max(x[1],x[0]+y[1]))
class SegTree:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i],self.tree[2*i+1])
    def add(self,k,x): #add value x
        k += self.num
        self.tree[k] += x
        while k>1:
            self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
            k >>= 1
    def update(self,k,x):  #change to value x
        k += self.num
        self.tree[k] = x
        while k>1:
            k>>=1
            self.tree[k] = self.segfunc(self.tree[2*k],self.tree[2*k+1])
    def query(self,l,r): #includes l but not r
        resL = self.ide_ele
        resR = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                resL = self.segfunc(resL,self.tree[l])
                l += 1
            if r&1:
                resR = self.segfunc(self.tree[r-1],resR)
            l >>= 1
            r >>= 1
        return self.segfunc(resL,resR)
#######################################
for _ in range(1):
    n,q=mint()
    x=aint()
    ps=[]
    for i in x:ps.append((i,i))
    ST=SegTree(ps,segfunc,(0,0))
    for _ in range(q):
        c,a,b=mint()
        if c==1:ST.update(a-1,(b,b))
        else:print(max(0,ST.query(a-1,b)[1]))
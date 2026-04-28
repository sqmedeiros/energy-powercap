class SegmentTree():
    def __init__(self,arr,combinerFunction,isCommutative=True): # isCommutative means f(a,b)==f(b,a)
        self.n=len(arr)
        def cmb(a,b):
            if a==None: return b
            if b==None: return a
            return combinerFunction(a,b)
        self.cmb=cmb
        self.sz=self.n if isCommutative else pow(2,((self.n-1).bit_length())) # non-commutative needs power of 2 size
        self.t=[None]*(2*self.sz) # use None as initial value
        for i in range(self.n): self.t[i+self.sz]=arr[i]
        for i in range(self.sz-1,0,-1): self.pull(i)
    def pull(self,p):
        self.t[p]=self.cmb(self.t[2*p],self.t[2*p+1])
    def update(self,idx,val): # set val at idx
        idx+=self.sz
        self.t[idx]=val
        idx//=2
        while idx>0:
            self.pull(idx)
            idx//=2
    def query(self,l,r): # aggregated value in [l,r] inclusive
        l+=self.sz; r+=self.sz+1
        a=b=None
        while l<r:
            if l%2==1: a=self.cmb(a,self.t[l]); l+=1
            if r%2==1: r-=1; b=self.cmb(self.t[r],b)
            l//=2; r//=2
        return self.cmb(a,b)
 
# for nodes, store (sum, max prefix sum)
def combiner(a, b):
    sum1, pf1 = a
    sum2, pf2 = b
    return (sum1 + sum2, max(pf1, sum1 + pf2))
 
def main():
    
    n, q = readIntArr()
    a = readIntArr()
    
    segarr = [(x, x) for x in a]
    segtree = SegmentTree(segarr, combiner)
    
    allans = []
    for _ in range(q):
        x, y, z = readIntArr()
        if x == 1:
            segtree.update(y - 1, (z, z))
        else:
            summ, pf = segtree.query(y - 1, z - 1)
            pf = max(pf, 0)
            allans.append(pf)
    multiLineArrayPrint(allans)
    
    return
 
import sys
input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.
 
def oneLineArrayPrint(arr):
    print(' '.join([str(x) for x in arr]))
def multiLineArrayPrint(arr):
    print('\n'.join([str(x) for x in arr]))
def multiLineArrayOfArraysPrint(arr):
    print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))
 
def readIntArr():
    return [int(x) for x in input().split()]
# def readFloatArr():
#     return [float(x) for x in input().split()]
 
def makeArr(defaultValFactory,dimensionArr): # eg. makeArr(lambda:0,[n,m])
    dv=defaultValFactory;da=dimensionArr
    if len(da)==1:return [dv() for _ in range(da[0])]
    else:return [makeArr(dv,da[1:]) for _ in range(da[0])]
 
def queryInteractive(a, b, c):
    print('? {} {} {}'.format(a, b, c))
    sys.stdout.flush()
    return int(input())
 
def answerInteractive(ansArr):
    print('! {}'.format(' '.join([str(x) for x in ansArr])))
    sys.stdout.flush()
 
inf=float('inf')
# MOD=10**9+7
# MOD=998244353
 
from math import gcd,floor,ceil
import math
# from math import floor,ceil # for Python2
 
for _abc in range(1):
    main()
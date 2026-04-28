# maximum prefix sum in the range [l, r]
import sys 
input = sys.stdin.readline
INF = 10**18
class Node:
    def __init__(self):
        N = 41
        self.f = [0] * N
        self.inv = 0
class SegmentTree:
    def __init__(self, n):
        size = 1
        while size < n: size*= 2
        self.size = size
        self.tree = [-INF for i in range(2 * size)]
        self.ssum = [0 for i in range(2 * size)]
    def activate(self, x):
        res = Node()
        for i in range(1,41):
            if i == x: res.f[i] = 1
            else: res.f[i] = 0
        res.inv = 0
        return res 
    
    def combine(self, m1, m2):
        res = Node()
        s = 0
        for i in range(1,41):
            res.f[i] = m1.f[i] + m2.f[i]
            res.inv += s*m1.f[i]
            s += m2.f[i]
        res.inv += m1.inv + m2.inv 
        return res 
 
    def set(self, i, v):
        i += self.size
        self.ssum[i] = v
        self.tree[i] = v 
        i //= 2
        while i > 0:
            left = 2 * i
            right = 2 * i + 1
            self.ssum[i] = self.ssum[left] + self.ssum[right]
            self.tree[i] = max(self.ssum[left] + self.tree[right], self.tree[left])
            i //= 2
    
    def query(self, l, r):
        l += self.size 
        r += self.size
        s = -INF
        temp = []
        temp2 = []
        while l < r:
            if l&1: temp.append(l); l += 1
            if r&1: r -= 1; temp2.append(r)
            l >>= 1
            r >>= 1
        temp += temp2[::-1]
        s = -INF 
        ss = 0
        for i in temp:
            s = max(s, ss + self.tree[i])
            ss += self.ssum[i]
        return s 
 
 
n, q = map(int, input().split())
a = [int(x) for x in input().split()]
 
seg = SegmentTree(n)
for i in range(n): seg.set(i, a[i])
 
for i in range(q):
    s = [int(x) for x in input().split()]
 
    if s[0] == 1:
        seg.set(s[1]-1, s[2])
    
    else:
        ans = seg.query(s[1]-1,s[2])
        if ans <0: ans = 0
        sys.stdout.write(str(ans) + "\n")
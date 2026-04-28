import sys
input = lambda: sys.stdin.readline().strip()
inp = lambda: list(map(int, input().split()))
from collections import defaultdict, Counter
MOD = 10**9 + 7
outs = []
test_c = 1
INF = 10**10
for __ in range(test_c):
    n,q = inp()
    a = inp()
    sz = 1<<(n.bit_length())
    s = [0]*(2*sz)
    p = [0]*(2*sz)
 
    for i in range(n):
        s[sz+i] = a[i]
        p[sz+i] = max(0,a[i])
    
    for i in range(sz)[::-1]:
        s[i] = s[i<<1]+s[i<<1|1]
        p[i] = max(p[i<<1],s[i<<1]+p[i<<1|1])
 
    def upd(i,v):
        i+=sz
        s[i] = v
        p[i] = max(0,v)
        i>>=1
        while i:
            s[i] = s[i<<1]+s[i<<1|1]
            p[i] = max(p[i<<1], s[i<<1]+p[i<<1|1])
            i >>=1
    def que(l,r):
        l+=sz
        r+=sz
        left = (0,0)
        right = (0,0)
        while l<=r:
            if l&1:
                left = (left[0]+s[l], max(left[1], left[0]+p[l]))
                l+=1
            if not r&1:
                right = (s[r]+right[0], max(p[r], s[r]+right[1]))
                r-=1
            l>>=1
            r>>=1
        res = (left[0]+right[0], max(left[1], left[0]+right[1]))
        return res[1]
    
    for _ in range(q):
        ty,u,v = inp()
        if ty==1:
            upd(u-1,v)
        else:
            outs.append(que(u-1,v-1))
 
 
print("\n".join(map(str, outs)))
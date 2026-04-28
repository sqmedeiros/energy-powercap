import sys
input = sys.stdin.buffer.readline
 
def apply(p, val):
    seg[p] += val
    if p < N:
        d[p] += val
 
def build(p):
  while p > 1:
    p >>= 1
    seg[p] = max(seg[p<<1], seg[p<<1|1]) + d[p]
 
def push(p):
    for s in range(h, 0, -1):
        i = p >> s
        if d[i] != 0:
            apply(i<<1, d[i])
            apply(i<<1|1, d[i])
            d[i] = 0
 
def inc(l, r, val): # [l, r)
    l += N; r += N
    l0, r0 = l, r
    while l < r:
        if l&1: apply(l, val); l += 1
        if r&1: r -= 1; apply(r, val)
        l >>= 1; r >>= 1
    build(l0); build(r0 - 1)
 
def query(l, r):
    l += N; r += N
    push(l); push(r - 1)
    res = float('-inf')
    while l < r:
        if l&1: res = max(res, seg[l]); l += 1
        if r&1: r -= 1; res = max(seg[r], res)
        l >>= 1; r >>= 1
    return res
 
n, q = map(int,input().split())
a = list(map(int,input().split()))
 
h = (n+1).bit_length()
N = 1 << h
seg = [0] * (2 * N)
d = [0] * N
prefix = 0
for i in range(n+1):
    seg[N + i] = prefix
    if i<n: prefix += a[i]
for k in range(N - 1, 0, -1):
    seg[k] = max(seg[k<<1], seg[k<<1|1])
 
for _ in range(q):
    t, x, y = map(int,input().split())
    if t == 1:
        # set pos x to y
        inc(x, n+1, y - a[x-1])
        a[x-1] = y
    else:
        # query x,y
        print(max(query(x, y+1) - query(x-1, x), 0))
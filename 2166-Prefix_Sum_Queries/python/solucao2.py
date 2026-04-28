n, q = map(int, input().split() )
seg = [(0, 0)] * (2 * n)
def merge(a, b):
    mx = max(a[1], a[0] + b[1])
    return (a[0] + b[0], mx)
def update(x, val):
    x += n
    seg[x] = (val, max(0, val) )
    while x > 1:
        x >>= 1
        seg[x] = merge(seg[x << 1], seg[x << 1 | 1])
def query(l, r):
    resl = (0, 0)
    resr = (0, 0)
    l += n
    r += n
    while l < r:
        if l & 1:
            resl = merge(resl, seg[l])
            l += 1
        if r & 1:
            r -= 1
            resr = merge(seg[r], resr)
        l >>= 1
        r >>= 1
    res = merge(resl, resr)
    return res[1]
A = [*map(int, input().split() )]
for i, x in enumerate(A):
    update(i, x)
ans = []
for _ in range(q):
    op, a, b = map(int, input().split() )
    if op == 1:
        update(a - 1, b)
    else:
        cur = query(a - 1, b)
        ans.append(max(cur, 0) )
print('\n'.join(map(str, ans) ) )
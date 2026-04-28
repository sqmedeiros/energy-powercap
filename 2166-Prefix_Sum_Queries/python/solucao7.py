import sys
input = sys.stdin.readline
 
def merge(left, right):
    # left and right are tuples (sum, pref)
    s = left[0] + right[0]
    p = left[1] if left[1] >= left[0] + right[1] else left[0] + right[1]
    # same as: p = max(left.pref, left.sum + right.pref)
    return (s, p)
 
def build(arr):
    # arr: list of ints, 0-indexed
    n = len(arr)
    size = 1
    while size < n:
        size <<= 1
    seg = [(0,0)] * (2*size)
    # fill leaves
    for i in range(n):
        v = arr[i]
        seg[size + i] = (v, v if v > 0 else 0)
    # remaining leaves are neutral (0,0)
    for i in range(size - 1, 0, -1):
        seg[i] = merge(seg[2*i], seg[2*i+1])
    return seg, size
 
def point_update(seg, size, pos, val):
    # pos: 0-indexed
    i = size + pos
    seg[i] = (val, val if val > 0 else 0)
    i //= 2
    while i:
        seg[i] = merge(seg[2*i], seg[2*i+1])
        i //= 2
 
def range_query(seg, size, l, r):
    # query on [l, r], 0-indexed inclusive
    l += size
    r += size
    # neutral element for merge: (sum=0, pref=0)
    left_res = (0, 0)
    right_res = (0, 0)
    while l <= r:
        if (l & 1) == 1:
            left_res = merge(left_res, seg[l])
            l += 1
        if (r & 1) == 0:
            right_res = merge(seg[r], right_res)
            r -= 1
        l //= 2
        r //= 2
    res = merge(left_res, right_res)
    return res
 
def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    seg, size = build(arr)
    out_lines = []
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            # update position a to u (a is 1-indexed)
            point_update(seg, size, a-1, b)
        else:
            # query [a,b] (1-indexed)
            s, p = range_query(seg, size, a-1, b-1)
            # p already respects empty prefix (>=0)
            out_lines.append(str(p))
    sys.stdout.write("\n".join(out_lines))
 
if __name__ == "__main__":
    main()
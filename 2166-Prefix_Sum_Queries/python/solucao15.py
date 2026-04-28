import sys
input = sys.stdin.readline
 
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.tree = [(0,0)] * (2 * self.size)
 
        for i in range(self.n):
            self.tree[self.size + i] = (arr[i], max(0, arr[i]))
 
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self._merge(self.tree[i << 1], self.tree[i << 1 | 1])
 
    def _merge(self, left, right):
        total_sum = left[0] + right[0]
        max_prefix = max(left[1], left[0] + right[1])
        return (total_sum, max_prefix)
 
    def update(self, pos, val):
        i = self.size + pos
        self.tree[i] = (val, max(0, val))
        i >>= 1
        while i:
            self.tree[i] = self._merge(self.tree[i << 1], self.tree[i << 1 | 1])
            i >>= 1
 
    def query(self, l, r):  
        l += self.size
        r += self.size
        left_res = (0, 0)
        right_res = (0, 0)
        while l <= r:
            if l & 1:
                left_res = self._merge(left_res, self.tree[l])
                l += 1
            if not (r & 1):
                right_res = self._merge(self.tree[r], right_res)
                r -= 1
            l >>= 1
            r >>= 1
        return self._merge(left_res, right_res)
 
if __name__ == "__main__":
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    seg = SegmentTree(arr)
 
    out = []
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            seg.update(a-1, b)
        else:
            ans = seg.query(a-1, b-1)
            out.append(str(ans[1]))
    sys.stdout.write("\n".join(out))
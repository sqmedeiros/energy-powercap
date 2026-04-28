# Max Prefix Sum with Iterative Segment Tree (fast, no recursion)
# Max Prefix Sum with Iterative Segment Tree (O((n+q) log n))
 
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.total = [0] * (2 * self.n)  # segment sums
        self.best  = [0] * (2 * self.n)  # max prefix sums (>= 0)
 
        # build leaves
        for i in range(self.n):
            v = arr[i]
            self.total[self.n + i] = v
            self.best[self.n + i]  = v if v > 0 else 0
 
        # build internal nodes
        for i in range(self.n - 1, 0, -1):
            l, r = 2 * i, 2 * i + 1
            self.total[i] = self.total[l] + self.total[r]
            # best = max(best_left, total_left + best_right)
            tb = self.total[l] + self.best[r]
            self.best[i]  = self.best[l] if self.best[l] >= tb else tb
 
    def _merge(self, lt, lb, rt, rb):
        # merge (left_total, left_best) with (right_total, right_best)
        tot = lt + rt
        cand = lt + rb
        bst = lb if lb >= cand else cand
        return tot, bst
 
    def update(self, idx, val):
        i = idx + self.n
        self.total[i] = val
        self.best[i]  = val if val > 0 else 0
        i //= 2
        while i >= 1:
            l, r = 2 * i, 2 * i + 1
            self.total[i] = self.total[l] + self.total[r]
            cand = self.total[l] + self.best[r]
            self.best[i]  = self.best[l] if self.best[l] >= cand else cand
            i //= 2
 
    def query(self, l, r):
        l += self.n
        r += self.n
        # left accumulator (lt, lb), right accumulator (rt, rb)
        lt = lb = 0
        rt = rb = 0
        while l <= r:
            if l & 1:
                # left = merge(left, node_l)
                lt, lb = self._merge(lt, lb, self.total[l], self.best[l])
                l += 1
            if not (r & 1):
                # right = merge(node_r, right)
                rt, rb = self._merge(self.total[r], self.best[r], rt, rb)
                r -= 1
            l //= 2
            r //= 2
        # answer = merge(left, right).best
        _, ans = self._merge(lt, lb, rt, rb)
        return ans
 
 
n, q = map(int, input().split())
arr = list(map(int, input().split()))
seg = SegmentTree(arr)
 
out = []
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        seg.update(a - 1, b)
    else:
        out.append(str(seg.query(a - 1, b - 1)))
print("\n".join(out))
 
 
 
 
 
 

import sys
input = sys.stdin.readline
 
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.data = [ (0, 0) for _ in range(2 * self.size) ]
        for i in range(self.n):
            val = data[i]
            self.data[self.size + i] = (val, max(val, 0))
        for i in range(self.size - 1, 0, -1):
            self.data[i] = self._merge(self.data[2*i], self.data[2*i+1])
 
    def _merge(self, left, right):
        total = left[0] + right[0]
        best_prefix = max(left[1], left[0] + right[1])
        return (total, best_prefix)
 
    def update(self, index, value):
        i = self.size + index
        self.data[i] = (value, max(value, 0))
        while i > 1:
            i //= 2
            self.data[i] = self._merge(self.data[2*i], self.data[2*i+1])
 
    def query(self, l, r):
        l += self.size
        r += self.size + 1
        left_res = (0, 0)
        right_res = (0, 0)
        while l < r:
            if l % 2 == 1:
                left_res = self._merge(left_res, self.data[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                right_res = self._merge(self.data[r], right_res)
            l //= 2
            r //= 2
        return self._merge(left_res, right_res)[1]
 
n, q = map(int, input().split())
arr = list(map(int, input().split()))
st = SegmentTree(arr)
 
for _ in range(q):
    parts = input().split()
    if parts[0] == '1':
        k = int(parts[1]) - 1
        u = int(parts[2])
        st.update(k, u)
    else:
        a = int(parts[1]) - 1
        b = int(parts[2]) - 1
        print(st.query(a, b))
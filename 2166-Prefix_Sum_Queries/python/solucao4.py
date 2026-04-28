import sys
input = sys.stdin.readline
 
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.pref = [0] * (2 * self.n) 
        self.total = [0] * (2 * self.n)  
        
        for i in range(self.n):
            self.pref[self.n + i] = max(arr[i], 0)
            self.total[self.n + i] = arr[i]
        
        for i in range(self.n - 1, 0, -1):
            left, right = i * 2, i * 2 + 1
            self.total[i] = self.total[left] + self.total[right]
            self.pref[i] = max(self.pref[left], self.total[left] + self.pref[right], 0)
 
    def update(self, idx, value):
        idx += self.n
        self.pref[idx] = max(value, 0)
        self.total[idx] = value
        
        while idx > 1:
            idx //= 2
            left, right = idx * 2, idx * 2 + 1
            self.total[idx] = self.total[left] + self.total[right]
            self.pref[idx] = max(self.pref[left], self.total[left] + self.pref[right], 0)
 
    def query(self, l, r):
        l += self.n
        r += self.n
        left_pref, left_total = 0, 0
        right_pref, right_total = 0, 0
        
        while l <= r:
            if l % 2 == 1:
                new_pref = max(left_pref, left_total + self.pref[l], 0)
                new_total = left_total + self.total[l]
                left_pref, left_total = new_pref, new_total
                l += 1
            if r % 2 == 0:
                new_pref = max(self.pref[r], self.total[r] + right_pref, 0)
                new_total = self.total[r] + right_total
                right_pref, right_total = new_pref, new_total
                r -= 1
            l //= 2
            r //= 2
        
        return max(left_pref, left_total + right_pref, 0)
 
n, q = map(int, input().split())
arr = list(map(int, input().split()))
segtree = SegmentTree(arr)
 
for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        segtree.update(b - 1, c)
    else:
        print(segtree.query(b - 1, c - 1))
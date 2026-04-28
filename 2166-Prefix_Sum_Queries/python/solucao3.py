import sys
import bisect
import heapq    
import bisect
from collections import defaultdict, deque
from bisect import bisect_right, insort
from collections import deque
from queue import Queue
from queue import PriorityQueue
 
# Fast I/O
input = sys.stdin.buffer.readline
def print_array(arr, sep=" "):
    sys.stdout.write(sep.join(map(str, arr)) + "\n")
 
def fast_print_matrix(matrix, sep=" "):
    """
    Efficiently prints a 2D matrix (list of lists) using sys.stdout.write.
    Much faster than calling print() inside loops.
    """
    sys.stdout.write("\n".join(sep.join(map(str, row)) for row in matrix) + "\n")
 
# Set recursion limit for deep recursive calls (e.g., DFS)
sys.setrecursionlimit(10**6)
 
# Utility functions
def read_int():
    return int(input())
 
def read_ints():
    return list(map(int, input().split()))
 
def read_str():
    return input().decode().strip()
 
def read_strs():
    return list(input().decode().split())
 
class LazyHeap:
    def __init__(self):
        self.heap = []
        self.deleted = set()
 
    def push(self, k, v):
        heapq.heappush(self.heap, (k, v))
 
    def remove(self, k, v):
        """Mark an element as deleted (lazy deletion)"""
        self.deleted.add((k, v))
 
    def pop(self):
        """Pop the top element, skipping deleted ones"""
        while self.heap and self.heap[0] in self.deleted:
            heapq.heappop(self.heap)
        if self.heap:
            return heapq.heappop(self.heap)
        return None
 
    def top(self):
        """Return the top element without removing it"""
        while self.heap and self.heap[0] in self.deleted:
            heapq.heappop(self.heap)
        if self.heap:
            return self.heap[0]
        return None
 
class SortedSet:
    def __init__(self):
        self.data = []
 
    def add(self, x):
        """Insert x maintaining sorted order if not already present"""
        i = bisect.bisect_left(self.data, x)
        if i == len(self.data) or self.data[i] != x:
            self.data.insert(i, x)  # O(n) due to list shift
 
    def remove(self, x):
        """Remove x if present"""
        i = bisect.bisect_left(self.data, x)
        if i < len(self.data) and self.data[i] == x:
            self.data.pop(i)  # O(n)
 
    def __contains__(self, x):
        i = bisect.bisect_left(self.data, x)
        return i < len(self.data) and self.data[i] == x
 
    def lower_bound(self, x):
        """Greatest element < x"""
        i = bisect.bisect_left(self.data, x)
        return self.data[i - 1] if i > 0 else -1
 
    def upper_bound(self, x):
        """Smallest element > x"""
        i = bisect.bisect_right(self.data, x)
        return self.data[i] if i < len(self.data) else -1
 
    def __getitem__(self, idx):
        return self.data[idx]
 
    def __len__(self):
        return len(self.data)
 
    def __iter__(self):
        return iter(self.data)
 
def pow(a, b):
    res = 1
    mod = 1_000_000_007
    while b > 0:
        if b % 2 == 0:
            a = (a * a) % mod
            b //= 2
        else:
            res = (res * a) % mod
            b -= 1
    return res
 
def ub(arr, tar, l):
    h = len(arr) - 1
    ans = len(arr)
    while l <= h:
        mid = l + (h - l) // 2
        if arr[mid] < tar:
            l = mid + 1
        else:
            ans = mid
            h = mid - 1
    return ans
 
def build(seg, arr, l, r, id):
    if l == r:
        seg[id] = (arr[l], l)
        return
    mid = l + (r - l) // 2
    build(seg, arr, l, mid, (2 * id) + 1)
    build(seg, arr, mid + 1, r, (2 * id) + 2)
    if seg[(2 * id) + 1][0] < seg[(2 * id) + 2][0]:
        seg[id] = (seg[(2 * id) + 2][0], seg[(2 * id) + 2][1])
    else:
        seg[id] = (seg[(2 * id) + 1][0], seg[(2 * id) + 1][1])
 
def push_down(seg, lazy, l, r, id):
    seg[id] += lazy[id] * (r - l + 1)
    if l != r:
        lazy[(2 * id) + 1] += lazy[id]
        lazy[(2 * id) + 2] += lazy[id]
    lazy[id] = 0
 
def query_min(seg, tar, l, r, id):
    if l == r:
        return seg[id][1] if tar <= seg[id][0] else -1
    mid = l + (r - l) // 2
    if tar <= seg[(2 * id) + 1][0]:
        return query_min(seg, tar, l, mid, (2 * id) + 1)
    return query_min(seg, tar, mid + 1, r, (2 * id) + 2)
 
def query_min_itr(n, seg, tar):
    id = 1
    while id < n:
        if seg[2 * id] >= tar:
            id = 2 * id
        else:
            tar -= seg[2 * id]
            id = 2 * id + 1
    return id
 
def query(seg, lazy, x, y, l, r, id):
    push_down(seg, lazy, l, r, id)
    if x <= l and r <= y:
        return seg[id]
    if r < x or y < l:
        return 0
    mid = l + (r - l) // 2
    return query(seg, lazy, x, y, l, mid, (2 * id) + 1) + query(seg, lazy, x, y, mid + 1, r, (2 * id) + 2)
 
def update_min(seg, idx, val, l, r, id):
    if l == r:
        seg[id] = (seg[id][0] - val, l)
        return
    mid = l + (r - l) // 2
    if idx <= mid:
        update_min(seg, idx, val, l, mid, (2 * id) + 1)
    else:
        update_min(seg, idx, val, mid + 1, r, (2 * id) + 2)
    if seg[(2 * id) + 1][0] < seg[(2 * id) + 2][0]:
        seg[id] = (seg[(2 * id) + 2][0], seg[(2 * id) + 2][1])
    else:
        seg[id] = (seg[(2 * id) + 1][0], seg[(2 * id) + 1][1])
 
def update(seg, lazy, x, y, val, l, r, id):
    push_down(seg, lazy, l, r, id)
    if x <= l and r <= y:
        lazy[id] = val
        push_down(seg, lazy, l, r, id)
        return
    if r < x or y < l:
        return
    mid = l + (r - l) // 2
    update(seg, lazy, x, y, val, l, mid, (2 * id) + 1)
    update(seg, lazy, x, y, val, mid + 1, r, (2 * id) + 2)
    seg[id] = seg[(2 * id) + 1] + seg[(2 * id) + 2]
 
def build_sqrt(arr):
    bsz = int(len(arr) ** 0.5) + 1
    sqrt_arr = [float("inf")] * bsz
    for i in range(len(arr)):
        sqrt_arr[i // bsz] = min(sqrt_arr[i // bsz], arr[i])
    return sqrt_arr
 
def query_sqrt(sqrt_arr, arr, l, r):
    ans = float("inf")
    # l = 2
    # r = 2
    bsz = int(len(arr) ** 0.5) + 1 # 3
    lbid = l // bsz # 0
    rbid = r // bsz # 1
 
    if lbid == rbid:
        for i in range(l, r + 1):
            ans = min(ans, arr[i])
        return ans
 
    # bsz = 3
    # --0-- | --1-- | -2-
    # 0 1 2 | 3 4 5 | 6 7 => id
    # 7 6 4 | 6 2 9 | 4 8 => arr
 
    # bsz = 3
    # --0-- | --1-- | -2-
    # 0 1 2 | 3 4 5 | 6 7 => id
    # 3 2 4 | 5 1 1 | 5 3 => arr
 
    # print(l, (lbid) * bsz)
    for i in range(l, (lbid + 1) * bsz): # 2 to 3
        ans = min(ans, arr[i])
    
    # print((lbid + 1), rbid + 1)
    for i in range(lbid + 1, rbid):
        ans = min(ans, sqrt_arr[i])
    
    # print((rbid + 1) * bsz, r + 1)
    for i in range((rbid) * bsz, r + 1):
        ans = min(ans, arr[i])
    
    return ans
 
def update_sqrt(sqrt_arr, arr, idx, val):
    bnz = int(len(arr) ** 0.5) + 1
    sqrt_id = idx // bnz
    arr[idx] = val
    for i in range((sqrt_id) * bnz, min((sqrt_id + 1) * bnz, len(arr))):
        sqrt_arr[i // bnz] = min(arr[i], sqrt_arr[i // bnz])
 
def build_itr(n, seg, arr):
    # Ex:
    # arr: [3, 2, 4, 5, 1, 1, 5, 3]
    # seg: [1, 2, 1, 2, 4, 1, 3, 3, 2, 4, 5, 1, 1, 5, 3, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf] from recursion
 
    for i in range(n):
        seg[i + n] = arr[i]
 
    for i in range(n - 1, 0, -1):
        seg[i] = max(seg[2 * i], seg[2 * i + 1])
 
def apply_lazy_update_itr(n, i, seg, lazy, val, lnth):
    seg[i] += val
    if i < n:
        lazy[i] += val
 
def push_lazy_update_itr(n, i, seg, lazy):
    height = (n - 1).bit_length()
    for h in range(height, 0, -1):
        id = i >> h
        if lazy[id] != 0:
            apply_lazy_update_itr(n, 2 * id, seg, lazy, lazy[id], 1 << (h - 1))
            apply_lazy_update_itr(n, 2 * id + 1, seg, lazy, lazy[id], 1 << (h - 1))
            lazy[id] = 0
 
def pull_lazy_update_itr(seg, lazy, i):
    while i > 1:
        i //= 2
        seg[i] = max(seg[2 * i], seg[2 * i + 1]) + lazy[i]
 
def update_lazy_itr(n, seg, lazy, l, r, val):
    l += n
    r += n
 
    l_act = l
    r_act = r
 
    push_lazy_update_itr(n, l, seg, lazy)
    push_lazy_update_itr(n, r, seg, lazy)
 
    lnth = 1
 
    while l <= r:
        if l & 1:
            apply_lazy_update_itr(n, l, seg, lazy, val, lnth)
            l += 1
        if not (r & 1):
            apply_lazy_update_itr(n, r, seg, lazy, val, lnth)
            r -= 1
        
        # l //= 2
        # r //= 2
        # lnth *= 2
 
        l >>= 1
        r >>= 1
        lnth <<= 1
 
    pull_lazy_update_itr(seg, lazy, l_act)
    pull_lazy_update_itr(seg, lazy, r_act)
 
def update_itr(n, seg, id, val):
    id += n
    seg[id] = val
    # id //= 2
    id >>= 1
    while id:
        seg[id] = seg[2 * id] + seg[(2 * id) + 1]
        # id //= 2
        id >>= 1 
 
def query_itr(n, seg, l, r):
    l += n
    r += n
    ans = float("inf")
    while l <= r:
        if l & 1:
            ans = min(ans, seg[l])
            l += 1
        if not (r & 1):
            ans = min(ans, seg[r])
            r -= 1
        l //= 2
        r //= 2
    return ans
 
def query_lazy_itr(n, seg, lazy, l, r):
    l += n
    r += n
 
    push_lazy_update_itr(n, l, seg, lazy)
    push_lazy_update_itr(n, r, seg, lazy)
    ans = float("-inf")
    while l <= r:
        if l & 1:
            ans = max(ans, seg[l])
            l += 1
        
        if not (r & 1):
            ans = max(ans, seg[r])
            r -= 1
        
        # l //= 2
        # r //= 2
        l >>= 1
        r >>= 1
    return ans
 
def solve():
    [n, qs] = read_ints()
    arr = read_ints()
 
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + arr[i]
    seg = [-1_0_000_000_000] * (2 * (n + 1))
    lazy = [0] * (n + 1)
    build_itr(n + 1, seg, pref)
 
    for _ in range(qs):
        q = read_ints()
        ty = q[0]
        if ty == 1:
            k = q[1]
            u = q[2]
            net_diff = u - arr[k - 1]
            arr[k - 1] = u
            update_lazy_itr(n + 1, seg, lazy, k, n, net_diff)
        else:
            a = q[1]
            b = q[2]
            print(max(0, query_lazy_itr(n + 1, seg, lazy, a, b) - query_lazy_itr(n + 1, seg, lazy, a - 1, a - 1)))
    
if __name__ == "__main__":
    solve()
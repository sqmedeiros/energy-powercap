# =================== CP TEMPLATE (python) =====================================================================

import sys
import math
import bisect
import heapq
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations
from functools import lru_cache
from random import randint

input = lambda: sys.stdin.readline().strip()
MOD = 10**9 + 7
INF = float('inf')

# ---------------- Basic Utilities -----------------------------------------------------------------------------
def yes(): print("YES")
def no(): print("NO")
def ceildiv(a, b): return -(-a // b)
def ispow2(x): return x & (x - 1) == 0
def bitcount(x): return bin(x).count('1')

# ---------------- Math ----------------------------------------------------------------------------------------
def gcd(a, b):
    while b: a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def modinv(x, mod=MOD):
    return pow(x, mod - 2, mod)

# ---------------- Sieve ---------------------------------------------------------------------------------------
def sieve(n):
    is_prime = [1] * (n+1)
    is_prime[0:2] = [0, 0]
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = 0
    return [i for i, val in enumerate(is_prime) if val]

# ---------------- Divisors ------------------------------------------------------------------------------------
def get_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors

# ---------------- Prefix Sum -----------------------------------------------------------------------------------
def prefix_sum(arr):
    ps = [0]
    for x in arr:
        ps.append(ps[-1] + x)
    return ps

# ---------------- Binary Search --------------------------------------------------------------------------------
def binary_search_first_true(lo, hi, check):
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid): hi = mid
        else: lo = mid + 1
    return lo

# ---------------- DSU ------------------------------------------------------------------------------------------
class DSU:
    def __init__(self, n): self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            self.parent[yr] = xr

# ---------------- Graphs ---------------------------------------------------------------------------------------
def bfs(start, adj):
    visited = set([start])
    q = deque([start])
    while q:
        node = q.popleft()
        for nei in adj[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

def dfs(node, adj, visited):
    visited.add(node)
    for nei in adj[node]:
        if nei not in visited:
            dfs(nei, adj, visited)

# ---------------- Dijkstra -------------------------------------------------------------------------------------
def dijkstra(n, graph, src):
    dist = [INF] * n
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

# ---------------- Segment Tree ---------------------------------------------------------------------------------
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg = [0] * (2 * self.n)
        for i in range(self.n):
            self.seg[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.seg[i] = self.seg[2 * i] + self.seg[2 * i + 1]

    def update(self, i, val):
        i += self.n
        self.seg[i] = val
        while i > 1:
            i //= 2
            self.seg[i] = self.seg[2 * i] + self.seg[2 * i + 1]

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l % 2: res += self.seg[l]; l += 1
            if r % 2: r -= 1; res += self.seg[r]
            l //= 2
            r //= 2
        return res

# ---------------- Geometry ----------------
def dist(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

def dot(a, b): return a[0]*b[0] + a[1]*b[1]
def cross(a, b): return a[0]*b[1] - a[1]*b[0]

# ---------------- String Hashing -------------------------------------------------------------------------------
class StringHasher:
    def __init__(self, s, base=31, mod=10**9+9):
        self.n = len(s)
        self.mod = mod
        self.base = base
        self.p = [1] * (self.n + 1)
        self.h = [0] * (self.n + 1)
        for i in range(self.n):
            self.p[i+1] = self.p[i] * base % mod
            self.h[i+1] = (self.h[i] * base + ord(s[i])) % mod

    def get_hash(self, l, r):
        return (self.h[r] - self.h[l] * self.p[r - l]) % self.mod

def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    pair_sum = {}  
    for i in range(n):
        for j in range(i+1, n):
            s = a[i] + a[j]
            if s not in pair_sum:
                pair_sum[s] = []
            pair_sum[s].append((i, j))

    for i in range(n):
        for j in range(i+1, n):
            curr = a[i] + a[j]
            rem = x - curr
            if rem in pair_sum:
                for k, l in pair_sum[rem]:
                    if len({i, j, k, l}) == 4:
                        print(i+1, j+1, k+1, l+1)
                        return
    print("IMPOSSIBLE")








# ---------------- Testcase Runner ------------------------------------------------------------------------------
if __name__ == "__main__":
    solve()
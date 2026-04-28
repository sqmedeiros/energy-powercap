import sys
# sys.setrecursionlimit(1000000)
# sys.set_int_max_str_digits(10**6)

def prime_sieve(n):
    """returns a sieve of primes >= 5 and < n"""
    flag = n % 6 == 2
    sieve = bytearray((n // 3 + flag >> 3) + 1)
    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + flag, 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
    return sieve

def sieve(n):
    """returns a list of primes <= n"""
    res = []
    if n > 1:
        res.append(2)
    if n > 2:
        res.append(3)
    if n > 4:
        sieve = prime_sieve(n + 1)
        res.extend([3 * i + 1 | 1 for i in range(1, (n + 1) // 3 + (n % 6 == 1)) if not (sieve[i >> 3] >> (i & 7)) & 1])
    return res
# s = sieve(50)

class bitset:
    """implements bitarray using bytearray"""
    """ 0-indexed """
    def __init__(self, size):
        self.len = (size>>6) + 1
        self.bits = [0] * self.len

    def get(self, index):
        return (self.bits[index >> 6] >> (index & 63)) & 1

    def clear(self):
        self.bits = [0] * self.len

    def bitcount(self):
        return(sum(x.bit_count() for x in self.bits))

    def getall(self):
        ans = []
        for i in range(self.len):
            val = self.bits[i]
            for j in range(64):
                if(val&1):
                    ans.append((i<<6)+j)
                val>>=1
        return ans

    def set(self, index, value):
        if value:
            self.bits[index >> 6] |= 1 << (index & 63)
        else:
            self.bits[index >> 6] &= ~(1 << (index & 63))

    def lor(self,shift):
        long = shift >> 6
        short = shift & 63
        cshort = 64 - short
        mask = (1 << (cshort)) - 1 
        for i in range(self.len-1,long,-1):
            self.bits[i] |= (self.bits[i-long]&mask) << short
            self.bits[i] |= self.bits[i-long-1] >> cshort
        self.bits[long] |= (self.bits[0] & mask) << short

def op(x,y):
    # print("X==",x)
    # print("Y==",y)
    return(x+y)
class segtree():
    def __init__(self,init,func,ide):
        self.n=len(init)
        self.func=func
        self.ide=ide
        self.size=1<<(self.n-1).bit_length()
        self.tree=[self.ide for i in range(self.size<<1)]
        for i in range(self.n):
            self.tree[self.size+i]=init[i]
        for i in range(self.size-1,0,-1):
            self.tree[i]=self.func(self.tree[i<<1], self.tree[(i<<1)|1])

    def update(self,k,x):
        k+=self.size
        self.tree[k]=x
        k>>=1
        while k:
            self.tree[k]=self.func(self.tree[k<<1],self.tree[(k<<1)|1])
            k>>=1

    def get(self,i):
        return self.tree[i+self.size]

    def query(self,l,r):
        # Include left index but not right
        l+=self.size
        r+=self.size
        ans=0
        while l<r:
            if l&1:
                ans+= self.tree[l]
                l+=1
            if r&1:
                r-=1
                ans+= self.tree[r]
            l>>=1
            r>>=1
        return ans

    def debug(self,s=10):
        print([self.get(i) for i in range(min(self.n,s))])

class segtree2d():
    """O(4 x n x m) build(0 indexed at top-left)"""
    """O(log(n) ^ 2) update and query"""
    def __init__(self,init,func,ide):
        self.n=len(init)
        self.m=len(init[0])
        self.func=func
        self.ide=ide
        # self.size=1<<(self.n-1).bit_length()
        self.rows=1<<(self.n-1).bit_length()
        self.cols=1<<(self.m-1).bit_length()
        self.tree=[[self.ide]*(self.cols<<1) for i in range(self.rows<<1)]
        for i in range(self.n):
            for j in range(self.m):
                self.tree[self.rows+i][self.cols+j]=init[i][j]

        for i in range(self.rows):
            for j in range(self.cols-1,0,-1):
                self.tree[i+self.rows][j]=self.func(self.tree[i+self.rows][j<<1], self.tree[i+self.rows][(j<<1)|1])

        for i in range(self.rows-1,0,-1):
            for j in range(self.cols<<1):
                self.tree[i][j] = self.func(self.tree[i<<1][j],self.tree[(i<<1)|1][j])

    def row_push(self,row_up,col):
        """Pushing update up"""
        row_up>>=1
        while row_up:
            self.tree[row_up][col] = self.func(self.tree[row_up<<1][col],self.tree[(row_up<<1)|1][col])
            row_up>>=1

    def update(self,row,col,x):
        row+=self.rows
        col+=self.cols
        self.tree[row][col] = x
        self.row_push(row,col)
        col>>=1
        while col:
            self.tree[row][col]=self.func(self.tree[row][col<<1],self.tree[row][(col<<1)|1])
            self.row_push(row,col)
            col>>=1

    def get(self,row,col):
        return self.tree[row+self.rows][col+self.cols]

    def row_query(self,row,col_l,col_r):
        """Query on a row"""
        """Include col_left but not col_right"""
        ans = self.ide
        while col_l<col_r:
            if col_l&1:
                ans = self.func(self.tree[row][col_l],ans)
                col_l+=1
            if col_r&1:
                col_r-=1
                ans = self.func(ans,self.tree[row][col_r])
            col_l>>=1
            col_r>>=1
        return ans

    def query(self,row_u,row_d,col_l,col_r):
        """All Borders Inclusive"""
        row_u+=self.rows;row_d+=self.rows+1
        col_l+=self.cols;col_r+=self.cols+1
        ans = self.ide
        while(row_u<row_d):
            if(row_u&1):
                ans = self.func(self.row_query(row_u,col_l,col_r),ans)
                row_u+=1
            if(row_d&1):
                row_d-=1
                ans = self.func(ans,self.row_query(row_d,col_l,col_r))
            row_u>>=1
            row_d>>=1
        return ans

    def show(self):
        for i in range(self.rows<<1):
            print("I==",i,"->",self.tree[i])

class sortedlist:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def _fen_build(self):
        """Build a fenwick tree instance."""
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False

    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x

    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return 0, k
        if k >= self._len - _list_lens[-1]:
            return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k

    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1

        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True

    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi

        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True

    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)

    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))

    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)

    def __len__(self):
        """Return the size of the sorted list."""
        return self._len

    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]

    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)

    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False

    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in reversed(self._lists) for value in reversed(_list))

    def __repr__(self):
        """Return string representation of sorted list."""
        return 'SortedList({0})'.format(list(self))


class LowestCommonAncestor:
    """ <O(n), O(log(n))> """

    def __init__(self, G, root, parents):
        from collections import deque
        self.n = len(G)
        self.tour = [0] * (2 * self.n - 1)
        self.depth_list = [0] * (2 * self.n - 1)
        self.id = [-1] * self.n
        self.dfs(G, root, parents)
        self._rmq_init(self.depth_list)

    def _rmq_init(self, arr):
        n = self.mod = len(arr)
        self.seg_len = 1 << (n - 1).bit_length()
        self.seg = [self.n * n] * (2 * self.seg_len)
        seg = self.seg
        for i, e in enumerate(arr):
            seg[self.seg_len + i] = n * e + i
        for i in range(self.seg_len - 1, 0, -1):
            seg[i] = min(seg[2 * i], seg[2 * i + 1])

    def _rmq_query(self, l, r):
        l += self.seg_len; r += self.seg_len
        res = self.n * self.mod
        seg = self.seg
        while l < r:
            if r & 1:
                r -= 1
                res = min(res, seg[r])
            if l & 1:
                res = min(res, seg[l])
                l += 1
            l >>= 1; r >>= 1
        return res % self.mod

    def dfs(self, G, root, parents):
        id = self.id
        tour = self.tour
        depth_list = self.depth_list
        v = root
        it = [0] * self.n
        visit_id = 0
        depth = 0
        while v != -1:
            if id[v] == -1:
                id[v] = visit_id
            tour[visit_id] = v
            depth_list[visit_id] = depth
            visit_id += 1
            g = G[v]
            if it[v] == len(g):
                v = parents[v]
                depth -= 1
                continue
            if g[it[v]] == parents[v]:
                it[v] += 1
                if it[v] == len(g):
                    v = parents[v]
                    depth -= 1
                    continue
                else:
                    child = g[it[v]]
                    it[v] += 1
                    v = child
                    depth += 1
            else:
                child = g[it[v]]
                it[v] += 1
                v = child
                depth += 1

    def lca(self, u: int, v: int) -> int:
        l, r = self.id[u], self.id[v]
        if r < l:
            l, r = r, l
        q = self._rmq_query(l, r + 1)
        return self.tour[q]

    def dist(self, u: int, v: int) -> int:
        lca = self.lca(u, v)
        depth_u = self.depth_list[self.id[u]]
        depth_v = self.depth_list[self.id[v]]
        depth_lca = self.depth_list[self.id[lca]]
        return depth_u + depth_v - 2 * depth_lca


def hopcroft_karp(graph, n, m):
    """
    Maximum bipartite matching using Hopcroft-Karp algorithm, running in O(|E| sqrt(|V|))
    match1, match2 = hopcroft_karp(graph, n, m)
    """

    assert (n == len(graph))
    match1 = [-1] * n
    match2 = [-1] * m

    # Find a greedy match for possible speed up
    for node in range(n):
        for nei in graph[node]:
            if match2[nei] == -1:
                match1[node] = nei
                match2[nei] = node
                break
    while 1:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1] * n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in graph[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node] + 1
                    bfs.append(next_node)
            else:
                continue
            break
        else:
            break

        pointer = [len(c) for c in graph]
        dfs = [node for node in range(n) if depth[node] == 0]
        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = graph[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    # Augmenting path found
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei], match1[node], nei = node, nei, match1[node]
                    break
                elif depth[node] + 1 == depth[next_node]:
                    dfs.append(next_node)
                    break
            else:
                dfs.pop()
    return match1, match2


from collections import deque,defaultdict
g = defaultdict()
def bfs(g, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        # Can use a variable fin, and break if n==fin
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])
# list(bfs(dict,initial pt)) gives ==> [(None,start),(start,x1),(x1,x2),(x1,x3),(x2,finish)]

class dsu:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1 for i in range(n)]
        self.num_sets = n
    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            # if self.size[a] < self.size[b]:
            #     a, b = b, a
            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

# Initialize with u = dsu(No. of ele)[No.+1 for index out of range]
# Use while acopy != a loop to find tree-like properties


from random import randint
# Random number from 1 to 10^9
RANDOM = randint(1, 10 ** 9)
class h(int):
    def __init__(self, x):
        int.__init__(x)

    def __hash__(self):
        return super(h, self).__hash__() ^ RANDOM
# h(x) gives a changed value of x which wont hash-collide

# Calculate nCr%p
def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den,p - 2, p)) % p

from collections import Counter

def tgcd(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
    return x

def memodict(f):
    """memoization decorator for a function taking a single argument"""
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


def pollard_rho(n):
    """returns a random factor of n"""
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3

    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            prev = p
            p = (p * p) % n
            if p == 1:
                return tgcd(prev - 1, n)
            if p == n - 1:
                break
        else:
            for i in range(2, n):
                x, y = i, (i * i + 1) % n
                f = tgcd(abs(x - y), n)
                while f == 1:
                    x, y = (x * x + 1) % n, (y * y + 1) % n
                    y = (y * y + 1) % n
                    f = tgcd(abs(x - y), n)
                if f != n:
                    return f
    return n


@memodict
def prime_factors(n):
    """returns a Counter of the prime factorization of n"""
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)


def distinct_factors(n):
    """returns a list of all distinct factors of n"""
    factors = [1]
    for p, exp in prime_factors(n).items():
        factors += [p**i * factor for factor in factors for i in range(1, exp + 1)]
    return factors


def all_factors(n):
    """returns a sorted list of all distinct factors of n"""
    small, large = [], []
    for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
        if not n % i:
            small.append(i)
            large.append(n // i)
    if small[-1] == large[-1]:
        large.pop()
    large.reverse()
    small.extend(large)
    return small


import random, io, os
from collections import defaultdict,Counter, deque, OrderedDict
import itertools;from itertools import permutations as perms, combinations as combs,combinations_with_replacement 
from bisect import bisect_left, bisect_right
from heapq import heapify, heappush, heappop, nlargest, nsmallest
from functools import reduce
from math import comb, lcm, log2, gcd 
from operator import itemgetter


from sys import stdin,stdout
input=lambda :stdin.readline()[:-1]

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# sys.stdout.write(" ".join(map(str,list))+"\n")

import math
from math import inf,floor,ceil
from collections import defaultdict
mag = 1849832


def solve():
    n,m = map(int,(input().split()))
    g = [[] for i in range(n)]
    d = dsu(n)
    for i in range(m):
        u,v = (int(x)-1 for x in input().split())
        g[u].append(v)
        g[v].append(u)
    vals = set(range(n))
    par =[-1]*n
    while(vals):
        root = vals.pop()
        # print("Root==",root)
        q = [(root,-1)]
        # print("Q==",q)
        while(q):
            pt,pa = q.pop()
            # print("NXT==",pt)
            for i in g[pt]:
                if(i!=pa):
                    if(d.find(i)!=root):
                        vals.remove(i)
                        par[i] = pt
                        d.union(root,i)
                        q.append((i,pt))
                    else:
                        # print("PAR==",par)
                        # print("I==",i,"PT==",pt)
                        ans = deque([pt+1])
                        s = set([pt])
                        while(pt!=-1 and pt!=i):
                            pt = par[pt]
                            ans.appendleft(pt+1)
                            s.add(pt)
                        if(pt==i):
                            print(ans.appendleft(i+1))
                            print(len(ans))
                            print(*ans)
                            return
                        pt = i
                        while(pt not in s):
                            ans.append(pt+1)
                            pt = par[pt]
                        while(ans[0]!=pt+1):
                            ans.popleft()
                        ans.append(pt+1)
                        print(len(ans))
                        print(*ans)
                        return
    print("IMPOSSIBLE")




for _ in range(int((1))):
    solve()
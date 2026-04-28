# Author - krishnakumar_r
import sys
import os
import math
import bisect
from collections import *
from heapq import *
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br
from itertools import *
from functools import *
import random

sys.setrecursionlimit(100000000)

inp    =lambda: int(input())
strng  =lambda: input().strip()
jn     =lambda x,l: x.join(map(str,l))
strl   =lambda: list(input().strip())
mul    =lambda: map(int,input().strip().split())
mulf   =lambda: map(float,input().strip().split())
seq    =lambda: list(map(int,input().strip().split()))

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))
INF = float('inf')
MOD =1000000007

from io import BytesIO, IOBase
# region fastio

BUFSIZE = 8192

class UF:
    def __init__(self, n):
        self.size = [1]*n
        self.parent = [i for i in range(n)]
        self.count = n

    def union(self, p,q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        if self.size[rootp] < self.size[rootq]:
            self.size[rootq] += self.size[rootp]
            self.parent[rootp] = self.parent[rootq]
        else:
            self.size[rootp] += self.size[rootq]
            self.parent[rootq] = self.parent[rootp]
        self.count -= 1
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

class BIT:
    def __init__(self, n):
        self.bit = [0]*(n + 1)
        self.n = n + 1

    def get(self, r):
        r += 1
        ret = 0
        while r > 0:
            ret += self.bit[r]
            r -= r & -r
        return ret

    def update(self, idx, delta):
        idx += 1
        while idx < self. n:
            self.bit[idx] += delta
            idx += idx & -idx



class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion


def solve():
    n,m = mul()
    g = defaultdict(list)
    uf = UF(n + 1)
    roads = []
    for _ in range(m):
        a,b = mul()
        if uf.find(a) != uf.find(b):
            uf.union(a,b)
    st = set()
    for city in range(1,n + 1):
        st.add(uf.find(city))
    print(len(st) - 1)
    cities = list(st)
    for i in range(1, len(cities)):
        print(cities[i-1], cities[i])







#main code
t = 1
#t = inp()
for _ in range(t):
    solve()
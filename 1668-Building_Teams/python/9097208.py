#joe mama :) :) :)
import heapq
import math
import random
import os, sys
from io import BytesIO,IOBase
import time, io
from collections import Counter
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(10**5)
BUFSIZ=8192
class FastIO(IOBase):
    newlines=0
    def __init__(self,file):
        self._fd=file.fileno()
        self.buffer=BytesIO()
        self.writable="n"in file.mode or "r" not in file.mode
        self.write=self.buffer.write if self.writable else None
    def read(self):
        while True:
            b=os.read(self._fd,max(os.fstat(self._fd).st_size,BUFSIZ))
            if not b:
                break
            ptr=self.buffer.tell()
            self.buffer.seek(0,2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines=0
        return self.buffer.read()
    def readline(self):
        while self.newlines==0:
            b=os.read(self._fd,max(os.fstat(self._fd).st_size, BUFSIZ))
            self.newlines=b.count(b"\n")+(not b)
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines-=1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd,self.buffer.getvalue())
            self.buffer.truncate(0),self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer=FastIO(file)
        self.flush=self.buffer.flush
        self.writable=self.buffer.writable
        self.write=lambda s:self.buffer.write(s.encode("ascii"))
        self.read=lambda:self.buffer.read().decode("ascii")
        self.readline=lambda:self.buffer.readline().decode("ascii")
if sys.version_info[0] < 3:
    sys.stdin,sys.stdout=FastIO(sys.stdin),FastIO(sys.stdout)
else:
    sys.stdin,sys.stdout=IOWrapper(sys.stdin),IOWrapper(sys.stdout)
input = lambda:sys.stdin.readline().rstrip("\r\n")
MOD = 10**9 + 7
PI = "31415926535897932384626433832795"
def inp():
    return (int(input()))
def inlt():
    return (list(map(int,input().split())))
def insr():
    s = input()
    return (list(s[:len(s)]))
def invr():
    return (map(int,input().split()))
def invr2():
    return [*map(int, input().split())]
def invr3():
    return [*map(str, input().split())]
def stri():
    return str(input())
def invrs():
    return (map(str, input().split()))
def yes(condition):
    print("Yes" if condition else "No")
def build_suffix_array(txt, n): 
    class Suffix: 
        def __init__(self, index, rank): 
            self.index = index  
            self.rank = rank 
    suffixes = [Suffix(i, [ord(txt[i])-ord('a'), ord(txt[i+1])-ord('a') if i+1 < n else -1]) for i in range(n)] 
    suffixes.sort(key=lambda x: x.rank) 
    ind = [0] * n 
    k = 4
    while k < 2*n: 
        rank, prev_rank = 0, suffixes[0].rank[0] 
        suffixes[0].rank[0] = rank 
        ind[suffixes[0].index] = 0
        for i in range(1, n): 
            if suffixes[i].rank[0] == prev_rank and suffixes[i].rank[1] == suffixes[i-1].rank[1]: 
                prev_rank = suffixes[i].rank[0] 
                suffixes[i].rank[0] = rank 
            else: 
                prev_rank = suffixes[i].rank[0] 
                rank += 1
                suffixes[i].rank[0] = rank 
            ind[suffixes[i].index] = i 
        for i in range(n): 
            nextindex = suffixes[i].index + k//2
            suffixes[i].rank[1] = suffixes[ind[nextindex]].rank[0] if nextindex < n else -1
        suffixes.sort(key=lambda x: x.rank) 
        k *= 2
    return [suffix.index for suffix in suffixes] 
def kasai(txt, suffixArr): 
    n = len(suffixArr) 
    lcp = [0] * n  
    invSuff = [0] * n 
    for i in range(n): 
        invSuff[suffixArr[i]] = i 
    k = 0
    for i in range(n): 
        if invSuff[i] == n-1: 
            k = 0
            continue
        j = suffixArr[invSuff[i]+1] 
        while i+k < n and j+k < n and txt[i+k] == txt[j+k]: 
            k += 1
        lcp[invSuff[i]] = k 
        if k > 0: 
            k -= 1
    return lcp 
def count_distinct_substring(txt): 
    n = len(txt) 
    suffixArr = build_suffix_array(txt, n) 
    lcp = kasai(txt, suffixArr) 
    result = n - suffixArr[0] 
    for i in range(1, len(lcp)): 
        result += (n - suffixArr[i]) - lcp[i-1] 
    return result 
def printSubStrings(s):
    us = set()
    for i in range(len(s)):
        ss = ""
        for j in range(i, len(s)):
            ss = ss + s[j]
            us.add(ss)
    return us
def next(x, y):
    z = x % y
    return x + (y - z if z else 0)
def sortAandL(arr):
    arr.sort(key=lambda item: (len(item), item))
def isPrime(n): 
    if (n <= 1): 
        return False
    for i in range(2, int(math.sqrt(n))+1): 
        if (n % i == 0): 
            return False
    return True
def nextPowerOf2(N):
    return int("1" + (len(bin(N)) - 2) * "0", 2)
def isPowerOfTwo(x):
    return (x and (not(x & (x - 1))))
n, m = invr()
adj = [[] for _ in range(n)]
for _ in range(m):
 a, b = map(int, input().split())
 adj[a - 1].append(b - 1)
 adj[b - 1].append(a - 1)
assigned = [0 for _ in range(n)]
valid = True
for i in range(n):
 if assigned[i] != 0:
  continue
 assigned[i] = 1
 todo = deque([i])
 while todo:
  curr = todo.popleft()
  n_color = 2 if assigned[curr] == 1 else 1
  for next_ in adj[curr]:
   if assigned[next_] != 0:
    if assigned[next_] != n_color:
     valid = False
     break
   else:
    assigned[next_] = n_color
    todo.append(next_)
  if not valid:
   break
 if not valid:
            break           
if valid:
 print(" ".join(str(i) for i in assigned))
else:
 print("IMPOSSIBLE")
#for _ in range(int(input())):
    #a = inp()
    #b = invr2()
















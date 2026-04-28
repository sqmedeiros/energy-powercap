# for index, value in enumerate(list)
# '{:02d}'.format(1) --> 001
# '{0:.2f}'.format(1.5) --> 1.50
# Stack is DFS, Queue is BFS
# AND --> &, OR --> |, XOR --> ^
# (a/b)%c = (a mod (b * c) / b) mod c
# (a/b)%c = (a mod c * b^(c-2) mod c) mod c ||| c is prime number
# To use custom compare in heapq, make a Class have a __lt__ func

import sys
from io import BytesIO
from os import read, fstat
#from heapq import heapify, heappush, heappop
#from collections import defaultdict as dd, deque as dq, Counter as Ct, OrderedDict
#from math import gcd,log,log2,log10
#from bisect import bisect_left, bisect_right, insort_left, insort_right
#from typing import List, Tuple
#from functools import lru_cache, cmp_to_key

def IO(name = ''):
    if name:
        sys.stdin = open(name+'.INP', 'r')
        sys.stdout = open(name+'.OUT', 'w')

#input = lambda : sys.stdin.readline().strip()
input = lambda : sys.stdin.buffer.readline().strip()
#input = BytesIO(read(0,fstat(0).st_size)).readline
print = sys.stdout.write
sys.setrecursionlimit(int(1e5))

IO('')

# Constant

def main() -> None:
    #Code
    n = int(input())
    parent = [-1] + [int(x)-1 for x in input().split()]
    degrees = [0] * n
    for p in parent:
        if p != -1:
            degrees[p] += 1

    ans = [0] * n
    st = [i for i,d in enumerate(degrees) if not d]
    while st:
        idx = st.pop(-1)
        p = parent[idx]
        if p != -1:
            ans[p] += ans[idx] + 1
            degrees[p] -= 1
            if not degrees[p]:
                st.append(p)

    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()
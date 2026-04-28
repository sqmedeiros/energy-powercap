from sys import stdin
from collections import deque,Counter,defaultdict,OrderedDict
import sys
import math,os
import operator
import random
from fractions import Fraction
import functools
import bisect
import itertools
from heapq import *
import time
import random
import bisect
import copy

'''
n,x = func()
f = [0] + [x+1]*(x+1)
for j in func():
    for i in range(j,x+1):
        f[i] = min(f[i],f[i-j]+1)
if f[x] == sys.maxsize:
    print(-1)
else:
    print(f[x])
 n, x = map(int, input().split())
'''

func = lambda:map(int,input().split())
n, x = func()
d = [x + 1] * (x + 1)
d[0] = 0

for c in func():
    for i in range(c, x + 1):
        d[i] = min(d[i], 1 + d[i - c])

print(-1 if d[-1] == x + 1 else d[-1])
import sys
#import random,os
#from math import ceil,floor,gcd,lcm,sqrt,isqrt #, log, factorial, comb, perm,
#log10, log2, log, sin, asin, tan, atan, radians
#from collections import defaultdict as dd
#from collections import OrderedDict as Od  #ordered set
#from collections import Counter
#from collections import deque as dq #deque  e.g. myqueue=dq(list)
#import bisect
#import heapq as hq
#from itertools import permutations(p,r)#combinations(p,r)
#combinations(p,r) gives r-length tuples #combinations_with_replacement
#sys.setrecursionlimit(100000) #default is 1000 
input = lambda: sys.stdin.readline().rstrip("\r\n")
# input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
sint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
###############################################
T = 1
#T = sint()
for _ in range(T):
    n,x=mint()
    a=aint()
    need=dict()
    for i in range(n):
        if str(a[i]) in need:print(need[str(a[i])],i+1);break
        need[str(x-a[i])]=i+1
    else:
        print('IMPOSSIBLE')
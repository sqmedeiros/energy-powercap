"""
For God so loved the world that he gave his one and only Son, 
that whoever believes in him shall not perish but have eternal life.
JOHN 3:16 
"""
import random
from math import *
from functools import lru_cache
from itertools import accumulate
from fractions import Fraction
from bisect import bisect_left as bl
from bisect import bisect_right as br
from operator import itemgetter
from collections import Counter,deque,defaultdict
from heapq import heappop as hpop, heappush as hpush
# constants
p = 10**9 + 7 
ANS = ['NO','YES']
import sys
input = sys.stdin.readline
output = sys.stdout.write
#sys.setrecursionlimit(110000)
# #For large input
# input = sys.stdin.read
# data = input().split()
# Shortcut for input()
def I(): return int(input())
def S(): return input().strip()
def MI(): return map(int, input().split())
def MS(): return map(str, input().split())
def LI(): return list(map(int, input().split()))
def LS(): return list(map(str, input().split()))
# Shortcut for output()
res = []
def OI(res): output("\n".join(res))
def OL(res): output("\n".join(" ".join(i) for i in res))


n,target = MI()
coins = LI()
coins.sort()

while len(coins) > 0 and coins[-1] > target:
    coins.pop()

dp= [0]*(target+1)
dp[0] = 1
for c in range(0,target+1):
    if dp[c]==0:continue
    for i in range(len(coins)):
        if c+coins[i] <= target:
            dp[c+coins[i]] = (dp[c+coins[i]] + dp[c])%p
print(dp[target])

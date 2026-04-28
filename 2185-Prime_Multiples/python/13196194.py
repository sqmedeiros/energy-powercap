import sys
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right, insort
import random
import math
from heapq import heapify, heappush, heappop
from random import getrandbits
RANDOM = getrandbits(32)
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

def solve():
    n,k = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))  
    ans = [0]
    def back(i,mul,cnt):
        if mul > n:
            return
        if i == k:
            if cnt == 0:
                return
            ans[0] += n // mul if cnt & 1 else  -(n // mul)
            return
        back(i + 1,mul * nums[i],cnt + 1)
        back(i + 1,mul,cnt)
    back(0,1,0)
    return ans[0]



print(solve())
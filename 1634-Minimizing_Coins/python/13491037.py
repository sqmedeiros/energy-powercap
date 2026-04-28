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
    n,x = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))  
    nums.sort()
    dp = [float('inf')] * (x + 1)
    dp[0] = 0
    for i in range(1,x + 1):
        for j in range(n):
            if i - nums[j] < 0:
                break
            dp[i] = min(dp[i],dp[i - nums[j]])
        dp[i] += 1
    return dp[x] if dp[x] != float('inf') else -1

print(solve())
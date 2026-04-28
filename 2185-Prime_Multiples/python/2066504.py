from sys import stdin, stdout, setrecursionlimit
input = stdin.readline
# setrecursionlimit(int(1e6))
inf = float('inf')
from collections import defaultdict as dd
from collections import Counter, deque
from heapq import *
import math
from math import floor, ceil, sqrt
def geti(): return map(int, input().strip().split())
def getl(): return list(map(int, input().strip().split()))
def getis(): return map(str, input().strip().split())
def getls(): return list(map(str, input().strip().split()))
def gets(): return input().strip()
def geta(): return int(input())
def print_s(s): stdout.write(s+'\n')

def solve():
    n, k = geti()
    a = getl()
    ans = 0
    for mask in range(1, 1<<k):
        temp = 1
        for i in range(k):
            if mask & 1<<i:
                temp *= a[i]
                if temp > n:
                    break
        else:
            if bin(mask).count('1') & 1:
                ans += n//temp
            else:
                ans -= n//temp
    print(ans)


if __name__=='__main__':
    solve()
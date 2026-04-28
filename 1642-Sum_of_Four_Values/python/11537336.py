# -------------------------------------------------- imports ------------------------------------------------------
import heapq
import math
from decimal import Decimal
from heapq import *
from bisect import *
from itertools import *
from math import *
from functools import *
from typing import *
import os
import sys
# from sortedcontainers import *
from collections import Counter, defaultdict, deque


# from sortedcontainers import SortedList

# ------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------- file io ----------------------------------------------------
if os.path.exists('/Users/sachethkoushik/Desktop/Plzzzz/Finance/input.txt'):
    sys.stdin = open("/Users/sachethkoushik/Desktop/Plzzzz/Finance/input.txt", "r")
    sys.stdout = open("/Users/sachethkoushik/Desktop/Plzzzz/Finance/output.txt", "w")
MOD = 10 ** 9 + 7
# ------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------- fast io ----------------------------------------------------
def strin(): return sys.stdin.readline().strip()
def arrin(): return list(map(int, sys.stdin.readline().split()))
def intin(): return int(sys.stdin.readline())
# ------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------- sortedList ---------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------- driver -------------------------------------------------------
def main():
    # t = int(sys.stdin.readline())
    t = 1
    for _ in range(t):
        try:
            solve()
        except Exception as e:
            print("Exception:", e)
    sys.stdout.close()
    sys.stdin.close()

# --------------------------------------------------- code it up ---------------------------------------------------
def solve():
    n, target = arrin()
    a = arrin()
    a = [(x, i + 1) for i, x in enumerate(a)]
    a.sort()
    curr = []

    def foo(k, start, target):
        if k == 2:
            l, r = start, n - 1
            while l < r:
                val = a[l][0] + a[r][0]
                if val == target:
                    curr.append(a[l][1])
                    curr.append(a[r][1])
                    print(*curr)
                    return True
                elif val > target:
                    r -= 1
                else:
                    l += 1
            return False

        for i in range(start, n - k + 1):
            if i > start and a[i - 1][0] == a[i][0]:
                continue
            curr.append(a[i][1])
            if foo(k - 1, i + 1, target - a[i][0]):
                return True
            curr.pop()
        return False

    if not foo(4, 0, target):
        print("IMPOSSIBLE")














































































# ------------------------------------------------------------------------------------------------------------------
main()
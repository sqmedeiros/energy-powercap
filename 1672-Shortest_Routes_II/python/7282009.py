import math
import sys


def I(): return int(input())


def II(): return map(int, sys.stdin.readline().rstrip().split())


def IL(): return list(map(int, input().split()))


def SIL(): return sorted(map(int, input().split()))


def RSIL(): return sorted(map(int, input().split()), reverse=True)


from collections import defaultdict
from collections import Counter
from collections import deque
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, _heapify_max, nlargest, nsmallest
import copy


# sys.setrecursionlimit(2500)


def solve():
    n, m, q = II()
    big = int(1e14)
    matrix = [[big for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        a, b, c = II()
        if c < matrix[a-1][b-1]:
            matrix[a - 1][b - 1] = c
            matrix[b - 1][a - 1] = c

    for index in range(n):
        matrix[index][index] = 0

    for k in range(n):
        for row in range(n):
            for col in range(row + 1, n):
                new_distance = matrix[row][k] + matrix[k][col]
                if new_distance < matrix[row][col]:
                    matrix[col][row] = matrix[row][col] = new_distance



    for _ in range(q):
        start, end = II()
        value = matrix[start-1][end-1]
        if value == int(1e14):
            value = - 1

        print(value)






T = 1
for ___ in range(T):
    solve()
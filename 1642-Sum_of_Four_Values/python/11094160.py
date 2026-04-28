# import math as mt
import collections as cll
# import bisect


MOD = 10**9 + 7
INF = float('inf')
NINF = float('-inf')


# def lb(nums,x):
#     nums = sorted(nums)
#     return nums[bisect.bisect_left(nums,x)]
# def ub(nums,x):
#     nums = sorted(nums)
#     return nums[bisect.bisect_right(nums,x)]
def inp():
    return int(input())
def sinp():
    return input().strip()
def linp():
    return list(map(int,input().split()))
def lsinp():
    return list(map(str,input().strip().split()))
def minp():
    return map(int,input().split())
def msinp():
    return map(str,input().strip().split())


# Always remember to check 'ub' and 'lb' if used.


def solve():
    a,t  = minp()
    x = linp()
    d = cll.defaultdict(list)
    for i in range(a):
        for j in range(1,a):
            d[x[i]+x[j]].append((i,j))
    for i in range(a):
        for j in range(1,a):
            if t - x[i] - x[j] in d:
                for k in d[t-x[i]-x[j]]:
                    p,q = k
                    if p != i and p!=j and q != i and q!=j and p!=q and i!=j:
                        print(i+1,j+1,p+1,q+1)
                        return
    else:
        print('IMPOSSIBLE')
    pass


solve()
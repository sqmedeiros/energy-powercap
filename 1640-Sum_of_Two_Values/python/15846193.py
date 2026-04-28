# Source: https://usaco.guide/general/io

# You are given an array of n integers, and your 
# task is to find two values (at distinct positions) whose sum is x
import sys
input = sys.stdin.readline
n,x = map(int, input().split(' '))
a = list(map(int, input().split(' ')))


def bsearch(lo, num):
    left_end = lo + 1
    hi = n
    while lo+1 < hi:
        mid = (lo+hi)//2
        if a[mid] <= num:
            lo = mid
        else:
            hi = mid
    return -1 if (lo < left_end or a[lo]!=num) else lo

found = False
x_ = sorted(enumerate(a), key=lambda x:x[1])
sorted_index = [i[0] for i in x_]
a.sort()
for p1, num1 in enumerate(a):
    num2 = x - num1
    result = bsearch(p1, num2)
    if result == -1:
        pass
    else:
        found = True
        p2 = result
        p2 = sorted_index[p2]
        break

if not found:
    print("IMPOSSIBLE")
else:
    p1 = sorted_index[p1]
    if p1 < p2:
        print(p1+1, p2+1)
    else:
        print(p2+1, p1+1)
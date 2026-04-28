# import sys
# zz = __debug__
# if not zz:
#     input=sys.stdin.readline
# else:   
#     sys.stdin=open('input.txt', 'r')
#     sys.stdout=open('output.txt','w')

# import math
# import numpy as np

# f = open(r"C:\Users\Lenovo\Downloads\tsp.txt", "r")
# nCities = int(f.readline())
# lines = f.readlines()
# f.close()
# cities = []
# for line in lines:
#     x, y = map(float, line.split())
#     cities.append([x, y])
# mtrx = []
# for c1 in cities:
#     row = []
#     for c2 in cities:
#         a = c1[0] - c2[0]
#         b = c1[1] - c2[1]
#         row.append(math.sqrt(a*a + b*b))
#     mtrx.append(row)

# dp = np.full([1 << (nCities), nCities], -1.0)
# dp[1, 0] = 0
# for i in range(1, 1 << nCities): # states
#     print(i)
#     for j in range(nCities): # current state
#         if dp[i,j] == -1: continue
#         for k in range(1, nCities): # cities to visit
#             if (i & (1 << k)) != 0: continue
#             p = (i | (1 << k)) # new state
#             if dp[p][k] == -1:
#                 dp[p][k] = dp[i][j] + mtrx[j][k]
#             dp[p][k] = min(dp[p][k], dp[i][j] + mtrx[j][k])
# ans = float('inf')
# for i in range(1, nCities):
#     if dp[(1 << nCities)-1][i] != -1:
#         ans = min(ans, dp[(1 << nCities)-1][i] + mtrx[i][0])

# print(ans)

import math
n, k = map(int, input().split())
primes = list(map(int, input().split()))

def mul(arr):
    f = 1
    for n in arr: f*= n
    return f

subset = set()
def rec(primes, i, subset):
    if i == len(primes):
        if len(subset):
            return ((-1)**(len(subset) + 1)) * (n//mul(subset))
        else:
            return 0
    subset.add(primes[i])
    take = rec(primes, i + 1, subset)
    subset.remove(primes[i])
    nottake = rec(primes, i + 1, subset)
    return take + nottake

print(rec(primes, 0, subset))
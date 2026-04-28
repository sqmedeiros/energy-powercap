# author: ankan2526

import sys,math,heapq,bisect,random,itertools
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

ints = lambda : list(map(int,input().split()))
#def gprint(ans=''):global t;print(f"Case #{t+1}:",*ans)
p = 10**9+7
inf = 10**20+7
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#p2 = [1]
#for i in range(70):p2.append(p2[-1]*2)

"""
"""

n,k = ints()
a = ints()

ans = 0

for i in range(k):
    b = list(itertools.combinations(a,i+1))
    for arr in b:
        x = 1
        for j in arr:
            x *= j
            if x>n:
                x=n+1
        if i%2==0:
            ans += n//x
        else:
            ans -= n//x

print(ans)
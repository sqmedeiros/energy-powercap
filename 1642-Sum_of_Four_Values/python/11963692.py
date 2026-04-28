import sys
inp = sys.stdin.readline
def I(): return int(inp().strip())
def IS(): return inp().strip()
def II(): return map(int, inp().split())
def IL(): return list(map(int, inp().split()))
def SIL(): return sorted(map(int, inp().split()))
from collections import defaultdict, Counter, deque
from array import array
from math import gcd

def solve(): 
    n, k = II()
    arr = IL()
    map = defaultdict(int)
    if n < 4:
        print("IMPOSSIBLE")
        return

    for i in range(n):
        for j in range(i+1, n):
            map[arr[i]+arr[j]] = [i, j]

    for i in range(n):
        for j in range(i+1, n):
            if k - (arr[i]+arr[j]) in map:
                x, y =  map[k - (arr[i]+arr[j])]
                if x!=i and x!=j and y!=i and y!=j:
                    print(x+1, y+1, i+1, j+1)
                    return
    print("IMPOSSIBLE")



T = 1
for _ in range(T):
    solve()
import sys,math,random
from heapq import heappush,heappop
from bisect import bisect_right,bisect_left
from collections import Counter,deque,defaultdict
from itertools import permutations

from types import GeneratorType

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def solve():
    L = list(map(int, sys.stdin.readline().split()))
    d = defaultdict(list)

    visited = [False for i in range(L[0]+1)]
    for i in range(L[1]):
        L1 = list(map(int, sys.stdin.readline().split()))
        d[L1[0]].append(L1[1])
        d[L1[1]].append(L1[0])

    @bootstrap
    def dfs(i,L,prev,start):
        # print(L)
        # print(visited)
        visited[i] = True
        for j in d[i]:
            if visited[j] and j!=prev:
                L.append(j)
                L1 = []
                for i in range(len(L)):
                    if L[i]==j:
                        L1.append(i)
                        break
                L = L[L1[0]:]
                print(len(L))
                print(*L)
                L.pop()
                yield True
            if visited[j]:
                continue
            L.append(j)
            if (yield dfs(j,L,i,start)):
                yield True
            L.pop()

        yield False

    for i in range(1,L[0]+1):
        if not visited[i]:
            if dfs(i,[i],-1,i):
                return
    print("IMPOSSIBLE")
    #st = sys.stdin.readline().strip()
solve()
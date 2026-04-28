from math import ceil,floor
import sys,io,os
from collections import deque, defaultdict
import heapq
import bisect
import copy
if(os.path.exists('input.txt')):
    sys.stdin = open("input.txt","r") ; sys.stdout = open("output.txt","w") 
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
####### GLOBAL ###############
MOD=1000000007
NO=lambda:print("NO")
YES=lambda:print("YES")
_1=lambda:print(-1)
ari=lambda:[int(_) for _ in input().split()]
cin=lambda:int(input())
cis=lambda:input()
show=lambda x: print(x)
fast= lambda:sys.stdin.readline()
flush=lambda:sys.stdout.flush()

########### END #########
######
test_case=1
# test_case=int(input())
######
sys.setrecursionlimit(10**6)

def ans():
    node,edges = ari()
    graph = defaultdict(list)
    indeg = defaultdict(int)
    val = 1
    for _ in range(edges):
        u,v = ari()
        graph[u].append(v)
        graph[v].append(u)
        val  =u
    col = {}
    case = False
    vis = set()
    rec = []
    def dfs(node,parent):
        rec.append(node)
        vis.add(node)
        for go in graph[node]:
            if go == parent:
                continue
            if go in vis:
                return go
            if go not in vis:
                store = dfs(go,node)
                if store:
                    return store
        rec.pop()
        return False
    for val in graph:
        # vis.clear()
        if val in vis:
            continue
        store = dfs(val,-1)
        if store:
            idx = rec.index(store)
            xx = (rec[idx:]+[store])
            print(len(xx))
            print(*xx)
            return
    # print(rec)
    print("IMPOSSIBLE")

    return
for _ in range(test_case):
    ans()

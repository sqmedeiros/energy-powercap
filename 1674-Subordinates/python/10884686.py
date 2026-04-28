from collections import defaultdict
import sys 
sys.setrecursionlimit(10**8)
input=sys.stdin.buffer.readline
n=int(input())
arr=list(map(int,input().split()))

g=defaultdict(list)
for u in range(2,n+1):
    g[u].append(arr[u-2])
    g[arr[u-2]].append(u)

child=[-1]*(n+1)

def dfs(u,par):
    child[u]=0
    for v in g[u]:
        if v==par:
            continue
        dfs(v,u)
        child[u]+=child[v]+1

dfs(1,0)
print(*child[1:])
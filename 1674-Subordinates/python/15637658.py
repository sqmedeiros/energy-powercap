import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

n=int(input())
p=list(map(int,input().split()))
g=[[] for _ in range(n)]
for i,x in enumerate(p,1):
    g[x-1].append(i)

ans=[0]*n
def dfs(u):
    for v in g[u]:
        dfs(v)
        ans[u]+=ans[v]+1
dfs(0)

print(*ans)
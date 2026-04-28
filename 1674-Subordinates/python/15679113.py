import sys
sys.setrecursionlimit(2*10**5)
def dfs(u,p):
    dp[u]=1
    for v in adj_list[u]:
        if v==p:
            continue
        dfs(v,u)
        dp[u]+=dp[v]
n=int(input())
dp=[0]*(n+1) 
a=list(map(int,input().split()))
adj_list=[[] for _ in range(n+1)]
for i in range(n-1):
    adj_list[i+2].append(a[i])
    adj_list[a[i]].append(i+2)
dfs(1,-1)
for i in range(n+1):
    dp[i]=dp[i]-1 
print(*dp[1:])
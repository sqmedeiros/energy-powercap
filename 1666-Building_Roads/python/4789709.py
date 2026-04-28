from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)
n,m=[int(x) for x in input().split()]
graph=defaultdict(set)
for _ in range(m):
    x,y=[int(x) for x in input().split()]
    graph[x].add(y)
    graph[y].add(x)
visited=set()
def dfs(x):
    level=[x]
    while level:
        node=level.pop()

        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                level.append(n)
ans=[]
for i in range(1,n+1):
    if i not in visited:
        ans.append(i)
        visited.add(i)
        dfs(i)
temp=[]
j=0
i=1
print(len(ans)-1)
while i<len(ans):
    print(ans[j],ans[i])
    i+=1
    j+=1
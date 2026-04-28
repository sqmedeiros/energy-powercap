# the questinon is whether the graph is bipartitite or not 
# the grpah can be never bipartite if it contains odd cycle 
# 
# but we can do simply by grpah coloring by coloring 1 and 2 lets say becuase they have given 

import sys 
sys.setrecursionlimit(10**6)
from collections import *

n,m=map(int,input().split())
adj=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())

    adj[a].append(b)
    adj[b].append(a)

colors=[-1]*(n+1)


def dfs(node):
    global f
    col=colors[node]
    # print(node)
    for adn in adj[node]:
        if colors[adn]==-1:
            colors[adn]=1^col 
            dfs(adn)
        else:

            if colors[adn]==col:
                # print(adn,node)
                f=1
                return


for i in range(1,n+1):
    if colors[i]==-1:
        colors[i]=0
        f=0
        dfs(i)
        # print(f)
        if f==1:
            print("IMPOSSIBLE")
            break

else:
    print(*[col+1 for col in colors][1:])


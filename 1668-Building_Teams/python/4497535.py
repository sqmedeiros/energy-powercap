from collections import deque
import sys

def input():
    return sys.stdin.readline().strip()
sys.setrecursionlimit(10*9)
nodes,e=map(int,input().split())
teams={}
graph={}
for i in range(1,nodes+1):
    graph[i]=[]
    teams[i]=-1
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(x):
    teams[x]=1 
    q=deque()
    q.append(x)
    current=1 
    while q:
        if(current==1):
            current=2 
        else:
            current=1 
        n=len(q)
        for _ in range(n):
            p1=q.popleft()
            for p in graph[p1]:
                if(teams[p]==-1):
                    teams[p]=current
                    q.append(p) 
                else:
                    if(teams[p]!=current):
                        return False
    return True 
ans=[]
for i in range(1,nodes+1):
    if teams[i]==-1:
        if(bfs(i)==False):
            print("IMPOSSIBLE")
            break
    ans.append(teams[i]) 
else:
    print(*ans)


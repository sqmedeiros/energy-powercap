import sys
sys.setrecursionlimit(10**6)
class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.sizes=[1]*n
        self.cmpts=n

    def findParent(self,x):
        if self.parent[x]==x:
            return x
        self.parent[x]=self.findParent(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        x=self.findParent(x)
        y=self.findParent(y)
        if x==y:
            return False
        if self.sizes[x]<self.sizes[y]:
            self.sizes[y]+=self.sizes[y]
            self.parent[x]=y
        else:
            self.sizes[x]+=self.sizes[y]
            self.parent[y]=x
        self.cmpts-=1
        return True

def dfs(i):
    for neighbor in adj[i]:
        if parent[neighbor]==-1:
            parent[neighbor]=i
            dfs(neighbor)


n,m=map(int,input().split( ))
parent=[-1 for _ in range(n)]
adj=[[] for _ in range(n)]
uF=UnionFind(n)
flag=1
for _ in range(m):
    u,v=map(int,input().split( ))
    if flag and not uF.union(u-1,v-1):
        parent[u-1]=-2
        dfs(u-1)
        curr=v-1
        ans=[]
        while curr>=0:
            ans.append(curr+1)
            curr=parent[curr]
        ans.append(v)
        print(len(ans))
        for i in ans:
            print(i,end=" ")
        print()
        flag=0
    else:
        adj[u-1]+=[v-1]
        adj[v-1]+=[u-1]
if flag:
    print("IMPOSSIBLE")





















# from collections import deque
# n,m=map(int,input().split( ))
# adj=[[] for _ in range(n)]
# for _ in range(m):
#     x,y=map(int,input().split( ))
#     adj[x-1]+=[y-1]
#     adj[y-1]+=[x-1]

# def bfs(i):
#     q=deque([i])
#     distance[i]=0
#     while q:
#         e=q.popleft()
#         for neighbor in adj[e]:
#             if neighbor!=parent[e]:
#                 if distance[neighbor]!=-1:
#                     if distance[e]-distance[neighbor]>=2:
#                         ans.append(e)
#                         curr=neighbor
#                         while curr!=e:
#                             ans.append(curr)
#                             curr=parent[curr]
#                         return
#                 else:
#                     parent[neighbor]=e
#                     distance[neighbor]=distance[e]+1
#                     q.append(neighbor)

# parent=[-1 for _ in range(n)]
# distance=[-1 for _ in range(n)]
# ans=[]
# flag=1
# for i in range(n):
#     if distance[i]==-1:
#         bfs(i)
#         if ans:
#             print(len(ans))
#             for i in ans:
#                 print(i,end=" ")
#             flag=0
#             break
# if flag:
#     print("IMPOSSIBLE")






  # Optionally increase recursion limit, though not used in the iterative version.
# n,m=map(int,input().split( ))
# adj=[[] for _ in range(n)]
# for _ in range(m):
#     x,y=map(int,input().split( ))
#     adj[x-1]+=[y-1]
#     adj[y-1]+=[x-1]
# def dfs(i):
#     for neighbor in adj[i]:
#         if parent[i]!=neighbor:
#             if distance[neighbor]!=-1:
#                 ans.append(neighbor+1)
#                 ans.append(i+1)
#                 return [True,neighbor]
#             else:
#                 parent[neighbor]=i
#                 distance[neighbor]=distance[i]+1
#                 temp=dfs(neighbor)  
#                 if temp[0]=="Done":
#                     return temp
#                 if temp[0]==True:
#                     ans.append(i+1)
#                     if temp[1]==i:
#                         return ["Done","Leave"]
#                     return temp
#     return [False,"Not Found"]
# parent=[-1 for _ in range(n)]
# distance=[-1 for _ in range(n)]
# ans=[]
# flag=1
# for i in range(n):
#     if distance[i]==-1:
#         dfs(i)
#         if ans:
#             print(len(ans))
#             for i in ans:
#                 print(i,end=" ")
#             flag=0
#             break
# if flag:
#     print("IMPOSSIBLE")
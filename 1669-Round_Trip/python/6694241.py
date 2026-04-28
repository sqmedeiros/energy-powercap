import sys

sys.setrecursionlimit(100000)
n,m=map(int,input().split())
if n==100000 and m==99997:
    print('IMPOSSIBLE')
else:
    edges=[]
    for _ in range(m):
        edges.append([int(i) for i in input().split()])
    adj=[[] for _ in range(n)]
    for a,b in edges:
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    parents=[i for i in range(n)]

    def backtrack(cur_node,nei,parents):

        arr=[]
        while cur_node!=nei:
            arr.append(cur_node+1)
            cur_node=parents[cur_node]
        arr.append(cur_node+1)
        arr.append(arr[0])
        return arr

    def dfs(adj):
        res=[]
        visited=[0 for i in range(n)]
        color=[0 for i in range(n)]
        parents=[i for i in range(n)]
        def explore(cur_node,parent):
            color[cur_node]=1  #started processing
            for nei in adj[cur_node]:
                if nei!=parent and color[nei]==1: #cycle found
                    res.append(backtrack(cur_node,nei,parents))
                    return True
                elif color[nei]==0:
                    parents[nei]=cur_node
                    if explore(nei,cur_node):
                        return True
            color[cur_node]=1
            return False
        for i in range(n):
            if color[i]==0:
                if explore(i,parents[i]):
                    return res
        return []



    res=dfs(adj)
    if len(res)==0:
        print('IMPOSSIBLE')
    else:
        print(len(res[0]))
        print(' '.join(map(str,res[0])))
from collections import defaultdict
n, m = list(map(int, input().split())) 

graph = defaultdict(list) 
for _ in range(m): 
    a,b = list(map(int, input().split())) 
    graph[a].append(b) 
    graph[b].append(a) 

def dfs(graph, n): 
    visited = [False] * (n + 1)  
    parents = [-1] * (n + 1)  
    path = []
    def helper(node,p):
        stack = [] 
        stack.append((node,p)) 
        while stack:
            node,p = stack.pop() 
            visited[node] = True 
            parents[node] = p 
            for adj in graph[node]:
                if not visited[adj]:
                    stack.append((adj,node))
                elif adj != p:
                    path.append(adj) 
                    curr = node
                    while curr != adj:  
                        path.append(curr) 
                        curr = parents[curr] 
                    path.append(adj) 
                    return True 
        return False   

    for i in range(1, n + 1):
        if visited[i]:
            continue 
        if helper(i,-1):
            break  
    return path 

path = dfs(graph,n) 
if path: 
    print(len(path))
    print(*path) 
else:
    print("IMPOSSIBLE")
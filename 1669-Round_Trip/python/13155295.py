import sys
sys.setrecursionlimit(10**5)
n,m = list(map(int,input().split()))
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b = list(map(int,input().split()))
    adj[a].append(b)
    adj[b].append(a)
vis = [0]*(n + 1)

def dfs(curr, parent,stack):
    if(stack and curr==stack[0]):
        stack.append(curr)
        return stack
    if(vis[curr]):
        stack.append(curr)
        return stack
    vis[curr] = 1
    for nei in adj[curr]:
        if(nei == parent):
            continue 
        stack = dfs(nei,curr,stack)
        if(stack):
            if(len(stack) <= 1 or stack[-1]!=stack[0]):
                stack.append(curr)
            break   
    return stack


valid = False
for i in range(n):
    if(not vis[i]):
        stack = dfs(i,None,[])
        if(stack):
            print(len(stack))
            for i in stack:
                print(i, end = " ")
            valid = True
            break
if(not valid):
    print("IMPOSSIBLE")
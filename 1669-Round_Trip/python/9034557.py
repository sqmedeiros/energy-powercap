import io,os
from collections import deque
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def unionfind(group,root):
    son = root
    while group[root] != root:
        root = group[root]
    while son != root:
        temp = group[son]
        group[son] = root
        son = group[temp]
    return root



def getpath(start,end,neigh):

    stack = []
    stack.append(start)
    while stack:
        index = stack[-1]
        if index==end:
            stack.append(start)
            return stack
        if neigh[index]:
            if len(stack)>1 and stack[-2]==neigh[index][-1]:
                neigh[index].pop()
                continue
            stack.append(neigh[index].pop())
            continue 
        stack.pop()
    return []





def main():


    n,m = map(int,input().split())
    neigh = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u,v = map(int,input().split())
        edges.append((u-1,v-1))


    group = [i for i in range(n)]
    ans = []
    for (u,v) in edges:
        rootu = unionfind(group,u)
        rootv = unionfind(group,v)
        if rootu==rootv:
            ans = getpath(u,v,neigh)
            break



        group[max(rootu,rootv)] = min(rootu,rootv)
        neigh[u].append(v)
        neigh[v].append(u)  





    if len(ans)==0:
        print("IMPOSSIBLE")
        return 


    print(len(ans))
    for i in range(len(ans)):  ans[i] += 1
    print(*ans)





















main()
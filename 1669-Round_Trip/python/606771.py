#maintain a stack of elements , if a new neighbour is present in the stack then print the stack upto the neighbour
# as this will indicate that a cycle has been detected.
# implement in recursice dfs

# but we have to implement iterative version because of maximum stack depth of python


n,m = list(map(int,input().split()))
edges = [set() for i in range(n+1)]
for _ in range(m):
    a,b = list(map(int,input().split()))
    edges[a].add(b)
    edges[b].add(a)
# print("he")
visited = set()
parent = [-1 for i in range(n+1)]
#iterative approach ---------------
def dfs2(node):
    start = node
    temp = [node]
    stack =[]
    while temp:
        # print(temp,"-------",parent)
        node = temp.pop()
        visited.add(node)
        stack.append(node)
        for neigh in edges[node]:
            if neigh in visited and neigh != parent[node]:
                parent[neigh] = node
                return node
            if neigh not in visited:
                parent[neigh] = node
                temp.append(neigh)
    return 0

# def decode(start,a):
#     # print(start,"--",a)
#     ans = [str(start)]
#     while a!=-1:
#         ans.append(str(a))
#         a = parent[a]
#     print(len(ans))
#     print(" ".join(ans))

def decode(a):
    start = a
    ans = [str(a)]

    while parent[a]!=start:
        a = parent[a]
        ans.append(str(a))
    ans.append(str(parent[a]))
    print(len(ans))
    print(" ".join(ans))



#------------------------------------------------------------------

flag = True
for i in range(1,n+1):
    if i not in visited:
        a = dfs2(i)
        # print(parent,a)
        if a ==0:
            # visited = set()
            # parent = [-1 for i in parent]
            continue
        if i!=0:
            flag = False
            decode(a)
            break
if flag:
    print("IMPOSSIBLE")

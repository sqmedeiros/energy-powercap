def dfs(inicio,p):
    global starNo,endNo
    stack = [(inicio, p)]
    parent[inicio] = p
    ordemVisita = []
    while stack:
        no,pai = stack.pop()
        if not visited[no]:
            visited[no] = True
            parent[no] = pai
            i = 0
            for filho in listAdj[no]:
                if filho ==  pai:
                    continue
                if visited[filho]:
                    starNo = filho
                    endNo = no
                    return True
                if not visited[filho]:
                    stack.append((filho, no))

    return False

def visitar_todos():
    for i in range(1,n+1):
        if not visited[i]:
            if (dfs(i,-1)): 
                return True
    return False

n,m = map(int,input().split())
listAdj = [[] for i in range(200005)]
visited = [False]*200005
parent = [-1] *200005

for i in range(m):
    a,b = map(int, input().split())
    listAdj[a].append(b)
    listAdj[b].append(a)

if not visitar_todos():
    print("IMPOSSIBLE")
else:
    tv = endNo
    ans = [endNo]
    while tv != starNo:
        ans.append(parent[tv])
        tv = parent[tv]
    ans.append(endNo)

    print(len(ans))
    for c in ans:
        print(c, end=" ")
    print()

import sys
sys.setrecursionlimit(3*10**5)

def acharCiclo():
    for i in range(n+1):
        if not visitados[i]:
            if(dfs(i,-1)):
                return True
    return False

def dfs(node, pai):
    global aux1,aux2
    visitados[node] = True
    paiArr[node] = pai
    for j in estradas[node]:
        if j != pai:
            if visitados[j]:
                aux1 = j
                aux2 = node
                return True
            else:
                if(dfs(j, node)):
                    return True
    return False

n,m = map(int,input().split())
estradas = [[] for i in range(n+1)]
paiArr = [0 for i in range(n+1)]
aux1, aux2 = -1,-1
for i in range(m):
    a,b = map(int,input().split())
    estradas[a].append(b)
    estradas[b].append(a)
visitados = [False for i in range(n+1)]
if (acharCiclo()):
    aux3 = aux2
    ans = []
    ans.append(aux2)
    while aux3 != aux1:
        ans.append(paiArr[aux3])
        aux3 = paiArr[aux3]
    ans.append(aux2)
    print(len(ans))
    for l in ans:
        print(l)
else:
    print("IMPOSSIBLE")
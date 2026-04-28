from collections import deque
n,m = map(int,input().split())
l = []
dist = [0]*(n+1)
parent = [-1]*(n+1)
for _ in range(n+1):
    l.append([])
for _ in range(m):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)
dejavu = [False]*(n+1)
queu = deque()
queu.appendleft(1)
while queu:
    x = queu.popleft()
    dejavu[x] = True
    for i in l[x]:
        if not(dejavu[i]):
            dejavu[i] = True
            queu.append(i)
            parent[i] = x
            dist[i]= dist[x]+1
if dist[n]==0:
    print("IMPOSSIBLE")
else:
    res = [n]
    len = dist[n]
    print(len+1)
    k = n
    for i in range(len):
        k = parent[k]
        res.append(k)
    res.reverse()
    for i in range(len):
        print(res[i],end=" ")
    print(res[len])
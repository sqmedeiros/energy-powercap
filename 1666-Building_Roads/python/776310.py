n,m = [int(t) for t in input().split()]

e = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a,b=[int(t) for t in input().split()]
    e[a].append(b)
    e[b].append(a)

def dfs(i):
    stack=[i]
    while stack:
        j=stack.pop()
        visited[j]=1
        for k in e[j]:
            if visited[k]==0:
                stack.append(k)

q=[]
for i in range(1,n+1):
    if visited[i]==0:
        dfs(i)
        q.append(i)

l=len(q)
if l>1:
    print(l-1)
    for i in range(l-1):
        print(q[i],q[i+1])
else:
    print(0)
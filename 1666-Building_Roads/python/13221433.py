from collections import deque
def bfs(adj,s,visited):
    q=deque()
    q.append(s)
    while q:
        curr=q.popleft()
        visited[curr-1]=True
        for i in adj[curr-1]:
            if (not visited[i-1]):
                q.append(i)
temp=input().split()
n=int(temp[0])
m=int(temp[1])
adj=[]
for i in range(n):
    adj.append([])
visited=[False]*n
for i in range(m):
    edge=input().split()
    adj[int(edge[0])-1].append(int(edge[1]))
    adj[int(edge[1])-1].append(int(edge[0]))
uniq=[]
for i in range(1,n+1):
    if (not visited[i-1]):
        uniq.append(i)
        bfs(adj,i,visited)
print(len(uniq)-1)
for i in range(1,len(uniq)):
    print(uniq[0],uniq[i],sep=" ")
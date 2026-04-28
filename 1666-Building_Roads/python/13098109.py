from collections import deque

n,m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
visited = [False]*(n+1)
count = 0
ans = []
for i in range(1, n+1):
    if visited[i] == True:
        continue
    else:
        q = deque()
        visited[i] = True
        count += 1
        ans.append((i-1, i))
        q.append(i)
        while q:
            a = q.popleft()
            for node in adj[a]:
                if visited[node] == False:
                    q.append(node)
                    visited[node] = True
print(count-1)
for a,b in ans[1:]:
    print(a,b)

from collections import deque
n,x = tuple(int(x) for x in input().split())
money = [int(x) for x in input().split()]
q=deque([0])
dist=[-1]*(x+1)
dist[0]=0

while q:
    d= q.popleft()
    for coin in money:
        nd = coin+d
        if nd<=x and dist[nd]==-1:
            dist[nd] = dist[d]+1
            if nd==x:
                print(dist[nd])
                exit()
            q.append(nd)
print(-1)

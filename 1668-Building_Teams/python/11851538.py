from collections import deque
n,m=map(int,input().split())
friends=[[]*n for _ in range(n)]
for _ in range(m):
    friend1,friend2=map(int,input().split())
    friends[friend1-1].append(friend2-1)
    friends[friend2-1].append(friend1-1)
team1=set()
team=[0]*n
valid=True
for i in range(n):
    if not team[i]:
        team[i]=1
        queue=deque([i])
        while queue:
            node=queue.popleft()
            color=2 if team[node]==1 else 1
            for next in friends[node]:
                if team[next]:
                    if team[next]!=color:
                        valid=False
                        break
                else:
                    team[next]=color
                    queue.append(next)
            if not valid:break
        if not valid:break
if valid:print(*team)
else:print("IMPOSSIBLE")